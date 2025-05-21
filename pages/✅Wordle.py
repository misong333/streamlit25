
def compare_words(guess, answer):
    result = []
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            result.append("🟩")  # 정답 위치
        elif guess[i] in answer:
            result.append("🟨")  # 다른 위치에 있음
        else:
            result.append("⬛")  # 없음
    return "".join(result)
import streamlit as st

# 정답 설정
ANSWER = "detroy"
MAX_TRIES = 6

# 세션 상태 초기화
if "tries" not in st.session_state:
    st.session_state.tries = []

st.title("🟩 Wordle Quiz")

guess = st.text_input("5글자 단어를 입력하세요", max_chars=5)

if st.button("제출"):
    guess = guess.lower()
    if len(guess) != 5:
        st.warning("5글자 단어를 입력해주세요.")
    else:
        result = compare_words(guess, ANSWER)
        st.session_state.tries.append((guess, result))

# 결과 출력
for word, res in st.session_state.tries:
    st.text(f"{word.upper()}  {res}")

# 정답 확인
if st.session_state.tries and st.session_state.tries[-1][0] == ANSWER:
    st.success("정답입니다! 🎉")
elif len(st.session_state.tries) >= MAX_TRIES:
    st.error(f"실패! 정답은 '{ANSWER.upper()}' 였습니다.")
