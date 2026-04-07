import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

# Euclidean distance measures how far apart two players are in terms of their raw stats. If two players have very similar attributes, they’ll be close in Euclidean terms. Cosine similarity, on the other hand, compares the “shape” of their stats—whether both players are strong in similar areas. Even if one player is overall stronger, cosine will show if their strengths are proportionally similar. In short, Euclidean is about absolute closeness, while cosine is about matching styles or patterns.


# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("fifa_clustered.csv")
X_scaled = joblib.load("X_scaled.pkl")

# -------------------------------
# PAGE SETTINGS
# -------------------------------
st.set_page_config(page_title="FIFA Player Recommender", layout="wide")

st.title("⚽ FIFA Player Recommendation System")
st.write("Select a player and get 5 similar replacement players for scouting.")

# -------------------------------
# RECOMMENDATION FUNCTION
# -------------------------------
# def get_similar_players_by_stats(player_name, df, X_scaled, n_recommendations=5, method='euclidean'):
#     try:
#         player_idx = df[df['short_name'] == player_name].index[0]
#     except:
#         return None

#     player_features = X_scaled[player_idx].reshape(1, -1)

#     if method == 'euclidean':
#         distances = euclidean_distances(player_features, X_scaled)[0]
#         similarities = 1 / (1 + distances)
#     else:
#         similarities = cosine_similarity(player_features, X_scaled)[0]

#     similar_indices = similarities.argsort()[::-1][1:n_recommendations+1]

#     results = df.iloc[similar_indices].copy()
#     results['similarity_score'] = similarities[similar_indices]

#     return results

def get_similar_players_by_stats(player_name, df, X_scaled, n_recommendations=5, method='euclidean'):
    try:
        player_idx = df[df['short_name'] == player_name].index[0]
    except:
        return None

    # Get selected player's cluster
    player_cluster = df.loc[player_idx, 'cluster']

    # Get all players in same cluster
    cluster_df = df[df['cluster'] == player_cluster]
    cluster_indices = cluster_df.index

    # Get selected player's scaled features
    player_features = X_scaled[player_idx].reshape(1, -1)

    # Get scaled features of same cluster players only
    cluster_features = X_scaled[cluster_indices]

    # Calculate similarity only within same cluster
    if method == 'euclidean':
        distances = euclidean_distances(player_features, cluster_features)[0]
        similarities = 1 / (1 + distances)
    else:
        similarities = cosine_similarity(player_features, cluster_features)[0]

    # Sort players by similarity
    sorted_idx = similarities.argsort()[::-1]

    # Convert cluster-relative indices back to original dataframe indices
    similar_indices = cluster_indices[sorted_idx]

    # Remove selected player itself
    similar_indices = [idx for idx in similar_indices if idx != player_idx][:n_recommendations]

    # Final recommended players
    results = df.loc[similar_indices].copy()
    results['similarity_score'] = [similarities[list(cluster_indices).index(idx)] for idx in similar_indices]

    return results

# -------------------------------
# PLAYER SELECTION
# -------------------------------
player_name = st.selectbox("Choose a Player", sorted(df['short_name'].dropna().unique()))

method = st.radio("Similarity Method", ["euclidean", "cosine"])

# -------------------------------
# SHOW SELECTED PLAYER INFO
# -------------------------------
selected_player = df[df['short_name'] == player_name].iloc[0]

st.subheader("🎯 Selected Player")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Overall", selected_player['overall'])
    st.metric("Pace", selected_player['pace'])

with col2:
    st.metric("Shooting", selected_player['shooting'])
    st.metric("Passing", selected_player['passing'])

with col3:
    st.metric("Defending", selected_player['defending'])
    st.metric("Physical", selected_player['physic'])

# -------------------------------
# RECOMMEND BUTTON
# -------------------------------
if st.button("Get Recommendations"):
    results = get_similar_players_by_stats(player_name, df, X_scaled, n_recommendations=5, method=method)

    if results is not None:
        st.subheader(f"🔍 Top 5 Similar Players to {player_name}")

        display_cols = ['short_name', 'overall', 'pace', 'shooting', 'passing', 'defending', 'physic', 'similarity_score']

        st.dataframe(results[display_cols].reset_index(drop=True), use_container_width=True)
    else:
        st.error("Player not found.")