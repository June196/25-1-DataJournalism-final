import streamlit as st
import pandas as pd
import numpy as np

snu_img_path = r"C:\Users\1126j\file for python\25-1 dataJ\final project_college university\snu_img.jpg"
snu_img = st.image(snu_img_path)


st.title("서울대 학부대학 설립과 융합교육")
st.subheader("서울대학교 학부대학이란 무엇인가? 어디로 가야하는가?")

st.write('지난해 말, 서울대학교는 새로운 형태의 교육조직인 학부대학을 공식 출범시키며 학부교육 혁신을 예고했다. "무전공 입학," "공통교양 강화," "마이크로디그리 신설" 같은 변화는 단순한 제도 개편을 넘어, 서울대가 학문 간 경계를 넘나드는 융합적 사고와 실천 중심의 교육을 핵심 가치로 삼기 시작했음을 보여준다. 이러한 움직임은 단지 내부의 조직 개편이 아니라, 대학 교육의 방향성을 근본부터 다시 묻는 시도라 할 수 있다.')
st.write('그렇다면, "학부대학"이란 무엇일까? 결코 낯선 개념은 아니다. 이미 미국을 비롯한 각국의 대학들은 수십 년 전부터 학부대학 체계를 운영해 왔고, 각자의 비전과 철학을 반영한 고유한 방식으로 교양교육과 전공 탐색을 지원해왔다. ')
st.write('몇 예시들을 통해 학부대학이란 무엇인지를 확인해보자.')

st.header("학부대학이란 무엇인가?")

# 사용자 입력 받기
st.subheader('서울대인의 목소리')
user_opinion = st.text_input('당신이 생각하는 융합교육이란 무엇인가요?')

"""
df = pd.DataFrame(columns=['opinion'])
if user_opinion:
    new_row = pd.DataFrame([[user_opinion]], columns=['opinion'])
    st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
"""

# 'df'가 st.session_state에 존재하지 않으면 초기화
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['opinion'])

# 사용자 의견이 입력되었을 때 데이터프레임에 추가
if user_opinion:
    new_row = pd.DataFrame([[user_opinion]], columns=['opinion'])
    st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)

# 데이터프레임 표시
st.write(st.session_state.df)
## 아니면 이거 wordcloud로 표시해볼까?




# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
df = pd.read_csv(r"C:\Users\1126j\file for python\25-1 dataJ\final project_college university\CourseList.csv")

# 데이터 구조 확인
print("열 목록:", df.columns.tolist())
print("\n데이터 미리보기:")
print(df.head())

# 영역별 교과목 수 계산 (DataFrame으로 변환)
area_counts_df = df['영역'].value_counts().reset_index()
area_counts_df.columns = ['영역', '교과목 수']

# 깔끔한 텍스트 출력
print("\n[공통교육 영역별 교과목 수]")
for _, row in area_counts_df.iterrows():
    print(f"{row['영역']}: {row['교과목 수']}개")

# 시각화 (barplot에 DataFrame 전달)
plt.figure(figsize=(8, 6))
sns.barplot(
    data=area_counts_df,
    x='교과목 수',
    y='영역',
    palette=sns.color_palette("viridis", len(area_counts_df))
)
plt.title('공통교육 영역별 교과목 수')
plt.xlabel('교과목 수')
plt.ylabel('공통교육 영역')
plt.tight_layout()
plt.show()

st.pyplot()
