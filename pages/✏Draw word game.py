import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

# --------------------------
# 단어 리스트
# --------------------------
words = ["apple", "dog", "house", "car", "book", "tree", "star", "fish", "sun", "ball"]

# --------------------------
# 초기 상태 설정
# --------------------------
if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(words)
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_number" not in st.session_state:
    st.session_state.question_number = 1
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# --------------------------
# 페이지 기본 설정
# --------------------------
st.set_page_config(page_title="Guess with the picture!", layout="centered")
st.title("🖼️ Let's draw and guess")

st.markdown(f"### 문제 {st.session_state.question_number}")
st.markdown(f"## 🎨 제시어: `{st.session_state.current_word.upper()}`")
st.write("👉 Look at the word and draw a picture. Let your friend guess the word by looking at the picture!")

# --------------------------
# 그림 그리는 캔버스
# --------------------------
canvas_result = st_canvas(
    fill_color="rgba(0, 0, 255, 0.3)",
    stroke_width=5,
    stroke_color="#000000",
    background_color="#ffffff",
    height=300,
    width=400,
    drawing_mode="freedraw",
    key="canvas",
)

st.divider()

# --------------------------
# 단어 맞히기 입력창
# --------------------------
st.subheader("Please type in the answer:")
user_guess = st.text_input("What does this picture represent?", key="guess_input")

if st.button("✅ Check the answer"):
    if user_guess.strip().lower() == st.session_state.current_word:
        st.session_state.score += 1
        st.session_state.feedback = "🎉 Correct! you got a +1 point."
    else:
        st.session_state.feedback = f"❌ Wrong. The answer was **{st.session_state.current_word.upper()}**."

    st.session_state.question_number += 1
    st.session_state.current_word = random.choice(words)
    st.experimental_rerun()

# --------------------------
# 점수 및 피드백
# --------------------------
if st.session_state.feedback:
    st.info(st.session_state.feedback)

st.markdown(f"### Current score: **{st.session_state.score}**")

if st.button("🔁 Moving on to the next topic"):
    st.session_state.current_word = random.choice(words)
    st.session_state.question_number += 1
    st.session_state.feedback = ""
    st.experimental_rerun()


