import streamlit as st

# 각 MBTI 유형에 맞는 휴식 방법 예시
mbti_recommendations = {
    "ISTJ": "조용한 공간에서 책을 읽거나 산책을 해보세요.",
    "ISFJ": "따뜻한 차 한 잔과 함께 편안하게 음악을 들어보세요.",
    "INFJ": "명상이나 일기 쓰기로 내면의 생각을 정리해 보세요.",
    "INTJ": "미래 계획을 세우거나 전략적 보드게임을 즐겨보세요.",
    "ISTP": "간단한 만들기나 퍼즐 맞추기 등의 활동적인 휴식이 좋아요.",
    "ISFP": "자연 풍경을 감상하거나 미술 활동을 해보세요.",
    "INFP": "좋아하는 드라마나 영화를 감상하거나 창작 활동을 권해요.",
    "INTP": "새로운 정보를 탐구하거나 논리 퍼즐을 해보세요.",
    "ESTP": "가벼운 운동이나 야외 스포츠를 추천해요.",
    "ESFP": "친구와 만남, 즐거운 음악 감상도 좋아요.",
    "ENFP": "창의적인 글쓰기나 취미 활동을 해보세요.",
    "ENTP": "재미있는 토론이나 즉흥 연설 등으로 에너지를 얻으세요.",
    "ESTJ": "향후 일정을 정리하거나 생산적인 휴식을 권해요.",
    "ESFJ": "가족, 친구와 따뜻한 시간을 보내보세요.",
    "ENFJ": "상담이나 대화로 감정을 나누는 것도 좋아요.",
    "ENTJ": "목표 설정과 미래 비전 계획 세우기를 추천해요."
}

st.set_page_config(page_title="MBTI 맞춤 휴식 상담소", page_icon="🧘‍♂️")

st.title("🧘‍♂️ MBTI 맞춤 휴식 추천 상담소")
st.write("아래에서 자신의 MBTI를 선택하면, 당신에게 딱 맞는 휴식 방법을 추천해드려요! 😊")

mbti_types = list(mbti_recommendations.keys())
user_mbti = st.selectbox("자신의 MBTI 유형을 선택하세요.", options=mbti_types)

if user_mbti:
    st.subheader(f"{user_mbti} 유형에게 추천하는 휴식 방법:")
    st.success(mbti_recommendations[user_mbti])

st.markdown("---")
st.write("💡 'MBTI'는 성격유형을 알려주는 검사입니다. 자신의 성향에 맞는 휴식 방법으로 더 행복한 하루 보내세요!")


# 실행 방법: 터미널에서 아래 명령어 입력
# streamlit run <파일명>.py

