import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="MBTI 휴식 추천 & 시각화")

# MBTI별 추천 레퍼런스
mbti_recommendations = {
    # (위에서 쓴 딕셔너리 그대로 사용)
    "ISTJ": "혼자 산책하거나 조용히 음악을 들어보세요.",
    "ISFJ": "따뜻한 차를 마시며 일기를 써보는 게 좋아요.",
    "INFJ": "조용한 공간에서 독서나 명상을 해보세요.",
    "INTJ": "퍼즐 혹은 전략 게임으로 두뇌를 쉬게 해보세요.",
    "ISTP": "가볍게 운동하거나 드라이브를 추천해요.",
    "ISFP": "그림 그리기나 사진 찍기 등을 해보세요.",
    "INFP": "감성적인 노래 듣기나 글쓰기를 해보세요.",
    "INTP": "새로운 지식 찾아보기나 취미 탐구를 해보세요.",
    "ESTP": "야외 스포츠나 즉흥적인 여행을 추천해요.",
    "ESFP": "친구들과 어울리며 신나는 활동을 해보세요.",
    "ENFP": "창의적인 취미(글쓰기, 그리기 등)를 추천해요.",
    "ENTP": "토론이나 새로운 아이디어 논의가 잘 맞아요.",
    "ESTJ": "계획을 세우는 시간이나 운동이 효과적이에요.",
    "ESFJ": "가족, 친구들과 따뜻한 대화를 나눠보세요.",
    "ENFJ": "누군가 도와주는 활동이나 리더십 활동도 좋아요.",
    "ENTJ": "목표 재설정, 자기계발 시간이 좋습니다."
}
mbti_types = list(mbti_recommendations.keys())

# 데이터 저장 파일 경로
DATA_PATH = "mbti_data.csv"

# 탭 분리
tab1, tab2 = st.tabs(["학생용 - 휴식 추천", "교사용 - MBTI 분포 시각화"])

with tab1:
    st.header("☺️ 내 MBTI로 추천받는 휴식 방법")
    name = st.text_input("이름을 입력하세요 (선택)")
    selected_mbti = st.selectbox("본인의 MBTI를 선택하세요", mbti_types)
    if st.button("제출하기"):
        st.success(f"추천 휴식법: {mbti_recommendations[selected_mbti]}")
        # 데이터 저장
        new_row = {"이름": name, "MBTI": selected_mbti}
        if os.path.exists(DATA_PATH):
            df = pd.read_csv(DATA_PATH)
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        else:
            df = pd.DataFrame([new_row])
        df.to_csv(DATA_PATH, index=False)
        st.info("선택한 MBTI 정보가 저장되었습니다.")

with tab2:
    st.header("📊 우리 반 MBTI 분포와 특징 파악")
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        # 이름 컬럼이 있다면 익명 처리
        st.write("※ 이름은 저장되지만 시각화에는 사용되지 않습니다.")
        mbti_counts = df['MBTI'].value_counts().reindex(mbti_types, fill_value=0)
        st.bar_chart(mbti_counts)
        # MBTI별 휴식법 리스트 추가로 보여주기
        show_tips = st.checkbox("MBTI별 추천 휴식법 전체 보기")
        if show_tips:
            for mbti, tip in mbti_recommendations.items():
                st.write(f"**{mbti}**: {tip}")
    else:
        st.warning("아직 제출된 데이터가 없습니다. 학생들이 먼저 MBTI를 선택해 주세요.")
