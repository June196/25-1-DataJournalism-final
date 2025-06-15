import streamlit as st
import pandas as pd
import numpy as np
import os
from wordcloud import WordCloud
from PIL import Image
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns


snu_img_path = "snu_img.jpg"
snu_img = st.image(snu_img_path, width=300)




st.title("서울대 학부대학 설립과 융합교육")
now = datetime.now().strftime("%Y.%m.%d. %H:%M")
st.markdown(
    f"""
    <p style='color: dark gray; font-size: 80%; margin-top: -5px; margin-bottom: 5px;'>
        기자: 권새미랑, 김석희, 박지윤  |  작성일: {now}  |  카테고리: 교양교육 · 융합교육  |  위치: 서울대학교
    </p>
    """,
    unsafe_allow_html=True
)

# margin 조정된 구분선
st.markdown("<hr style='border: 0.5px solid #ccc; margin-top: 5px; margin-bottom: 20px;'>", unsafe_allow_html=True)



st.markdown(f"""
<div style='font-size:100%; color:#333; line-height:1.6;'>
    <p margin-bottom: 20px;'>
        지난해 말, 서울대학교는 새로운 형태의 교육조직인 학부대학을 공식 출범시키며 학부교육 혁신을 예고했다. 
        "무전공 입학," "공통교양 강화," "마이크로디그리 신설" 같은 변화는 단순한 제도 개편을 넘어, 
        서울대가 학문 간 경계를 넘나드는 융합적 사고와 실천 중심의 교육을 핵심 가치로 삼기 시작했음을 보여준다. 
        이러한 움직임은 단지 내부의 조직 개편이 아니라, 대학 교육의 방향성을 근본부터 다시 묻는 시도라 할 수 있다.
    </p>
</div>
""", unsafe_allow_html=True)


st.subheader("학부대학이란 무엇인가?")
st.markdown(f"""
<div style='font-size:100%; color:#333; line-height:1.6;'>
    <p margin-bottom: 20px;'>
        그렇다면, "학부대학"이란 무엇일까? 결코 낯선 개념은 아니다. 이미 미국을 비롯한 각국의 대학들은 수십 년 전부터 학부대학 체계를 운영해 왔고, 
        각자의 비전과 철학을 반영한 고유한 방식으로 교양교육과 전공 탐색을 지원해왔다. 몇 예시들을 통해 학부대학이란 무엇인지를 확인해보자.
    </p>
</div>
""", unsafe_allow_html=True)



# 데이터 불러오기
df = pd.read_excel("USA_college_university.xlsx")

# 선택창
college_names = df['univ_name'].tolist()
selected_college = st.selectbox("대학을 선택하세요", college_names)

# 선택된 데이터
college_data = df[df['univ_name'] == selected_college].iloc[0]
img_path = college_data['img_path'].strip('"')

st.image(img_path, width=200)

st.markdown(f"""
<blockquote style='font-size:140%; color:#333;'>
    <strong>{college_data['univ_name']}</strong>의 Vision  
</blockquote>
""", unsafe_allow_html=True)



with st.expander("Vision 원문 보기"):
    st.markdown(
        f"<div style='color:gray; font-size:70%; white-space:pre-wrap;'>{college_data['vision_text']}</div>",
        unsafe_allow_html=True
    )



st.markdown(college_data['vision_sum'])

st.markdown(f"""
<blockquote style='font-size:140%; color:#333;'>
    <strong>{college_data['univ_name']}</strong>의 Vision 실현 방안  
</blockquote>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 10])

with col1:
    st.markdown("")
with col2:
    st.markdown("")
    

st.markdown("---")







# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
df = pd.read_csv("CourseList.csv")

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
fig1 = plt.gcf()
st.pyplot(fig1)



"""
융합교육에 대한 서울대인의 목소리
"""
st.subheader('서울대인의 목소리')
user_opinion = st.text_input('당신이 생각하는 융합교육이란 무엇인가요?')

# CSV 경로 지정
csv_path = "opinions.csv"

# CSV가 존재하면 불러오고, 없으면 빈 데이터프레임 생성
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=['opinion'])

# 사용자 입력이 있을 경우 추가
if user_opinion:
    new_row = pd.DataFrame([[user_opinion]], columns=['opinion'])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(csv_path, index=False)  # CSV로 저장

# WordCloud 생성 및 표시
if not df.empty:
    text = ' '.join(df['opinion'].dropna().astype(str))
    wordcloud = WordCloud(font_path='NotoSansKR-Bold.ttf', width=800, height=400, background_color='white').generate(text)
    
    st.subheader("융합교육에 대한 서울대인의 생각")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)




