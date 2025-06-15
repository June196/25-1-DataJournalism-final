import streamlit as st
import pandas as pd
import numpy as np
import os
from wordcloud import WordCloud
from PIL import Image
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import re

#SNU color 팔레트
snu_blue = 'rgb(15, 15, 112)'
snu_beige = 'rgb(220, 218, 178)'
snu_gray = 'rgb(102, 102, 102)'
snu_gold = 'rgb(139,111,77)'
snu_silver = 'rgb(139,141,143)'



snu_img_path = "snu_img.jpg"
snu_img = st.image(snu_img_path, width=300)



## 제목
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
#st.markdown("<hr style='border: 0.5px solid #ccc; margin-top: 5px; margin-bottom: 20px;'>", unsafe_allow_html=True)
st.markdown("---")

## 서론
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


## 본론 1: 학부대학이란 무엇인가?
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



## 본론 2: 서울대 학부대학_교양교육과정
st.subheader("서울대학교 학부대학")

st.markdown(f"""
<div style='font-size:100%; color:#333; line-height:1.6;'>
    <p>
        2025학년도부터 서울대학교 학부대학은 공통교양 교육과정을 전면 개편했다.
        이번 개편은 단순한 과목 조정이 아닌, 공통교양의 철학과 방향성 자체를 재설정한 일종의 선언에 가깝다.
        학문 수행을 위한 기초 역량부터 인간과 사회에 대한 이해, 그리고 공적 책임에 대한 성찰까지,
        서울대는 교양 교육을 통해 무엇을 가르치고자 하는지를 다시 묻고 있다.
        특히 이번 개편에서 주목할 만한 지점은 '베리타스(Veritas)' 영역의 신설이다.
    </p>
    <p>
        기존의 서울대 공통교양은 세 가지 영역, 즉 '학문의 토대', '지성의 열쇠', '지성의 확장'으로 분류되었다.
        이 중 '학문의 토대'는 글쓰기, 외국어, 수학, 과학, 컴퓨팅 등 학문 수행을 위한 도구적 능력을 다루는 영역이며,
        '지성의 열쇠'는 역사적 탐구, 철학적 사고, 문화 해석 등 인문학 중심의 교과목들이 분포한다.
        '지성의 확장'은 보다 창의적인 탐색이나 자기주도적 학습, 공감·소통 등을 포함하는 비교적 유연한 영역으로 설계되어 있다.
        이번 개편에서 여기에 추가된 '베리타스'는 공동체적 가치와 실천 윤리를 중심에 둔 교과목들을 아우르며,
        서울대 교양 교육이 지향하는 인재상에 마지막 조각을 더하는 역할을 한다.
    </p>
    <p>
        이러한 개편은 학부대학이라는 새로운 틀과 함께 진행되었다는 점에서 더욱 중요하다.
        학부대학은 단순히 교육과정을 관리하는 조직이 아니라,
        <b>서울대가 어떤 방향의 학부교육을 상상하고 설계하는지 그 비전을 구체화하는 플랫폼</b>이기도 하다.
        무전공 입학이라는 제도는 특정 전공 중심의 선발과 배치를 넘어서,
        학생 스스로가 다양한 학문을 탐색하고 스스로의 문제의식을 중심에 둔 전공 설계가 가능하도록 하는 기반이다.
        이 과정에서 교양교육, 특히 공통교양은 학문 탐색 이전에 반드시 거쳐야 할 사고의 훈련, 관점의 전환, 그리고 사회적 성찰의 장으로서 기능한다.
        그 중심에 베리타스가 놓인 것이다.
    </p>
    <p>
        그렇다면 현재 공통교양의 각 영역은 실제로 어떻게 구성되어 있을까?
        교과목 수 기준으로 살펴보면, '지성의 열쇠'가 206개로 가장 많은 과목을 포함하고 있으며,
        '지성의 확장'과 '학문의 토대'가 각각 175개와 171개로 뒤를 잇는다.
        반면, 새롭게 등장한 '베리타스'는 총 40개 과목으로 구성되어 있어 전체 공통교양 중 약 6.8%만을 차지한다.
        이는 단지 신설된 지 얼마 되지 않아 과목 수가 적은 수준을 넘어,
        그 개설 비중이 여전히 구조적으로 제한되어 있다는 점을 보여준다.
    </p>
    </div>
""", unsafe_allow_html=True)
            

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
df = pd.read_csv("CourseList.csv")

# 컬럼 이름에 공백이 있으면 제거
df.columns = df.columns.str.strip()

# 영역별 교과목 수 계산
area_counts_df = df['영역'].value_counts().reset_index()
area_counts_df.columns = ['영역', '교과목 수']
area_counts_df['영역'] = area_counts_df['영역'].apply(lambda x: re.sub(r"[A-Za-z]+", "", x).strip())


# Altair 차트 그리기
bar_chart = alt.Chart(area_counts_df).mark_bar().encode(
    x=alt.X('교과목 수:Q', title='교과목 수'),
    y=alt.Y('영역:N', sort='-x', title=' '),
    color=alt.Color('영역:N', scale=alt.Scale(domain=['지성의 열쇠', '지성의 확장', '학문의 토대', '베리타스'], range=[snu_blue, snu_silver, snu_gray, snu_beige]), legend=None),
    tooltip=['영역', '교과목 수']
).properties(
    width=600,
    height=400,
    title='공통교육 영역별 교과목 수 막대그래프'
).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).configure_title(
    fontSize=14,
    anchor='start'
)

# 출력
st.altair_chart(bar_chart, use_container_width=True)
st.caption("※ 데이터 기준: 2024년 2학기 서울대학교 공통교양 교과목 목록")



st.markdown(f"""
<div style='font-size:100%; color:#333; line-height:1.6;'>
    <p>
        실제로 WordCloud 분석에서도 베리타스 영역은 다른 영역에 비해 상대적으로 적은 수의 키워드만이 시각적으로 나타난다.
        이는 과목 수의 부족뿐 아니라, 베리타스 교과목이 특정 분야나 전공 지식보다는 가치 중심적 내용으로 구성되어 있어
        텍스트 기반의 키워드 추출에서도 비교적 약하게 드러나기 때문이다.
    </p>
    </div>
""", unsafe_allow_html=True)

# 데이터 불러오기
df = pd.read_csv('CourseList.csv')
korean_font = './NotoSansKR-Bold.ttf'

# SNU 컬러 팔레트
snu_palette = ['rgb(15, 15, 112)',
               'rgb(220, 218, 178)',
               'rgb(102, 102, 102)',
               'rgb(139,111,77)',
               'rgb(139,141,143)']

# 색상 함수 정의
import random
def snu_color_func(word, font_size, position, orientation, font_path, random_state):
    return random.choice(snu_palette)

# 워드클라우드 함수
def generate_wordcloud_by_area(df, font_path):
    unique_areas = df['영역'].dropna().unique()
    n_cols = 2
    n_rows = (len(unique_areas) + 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(14, 4 * n_rows))
    axes = axes.flatten()

    for i, area in enumerate(unique_areas):
        area_df = df[df['영역'] == area]
        text = " ".join(area_df['교과목명'].astype(str))

        wordcloud = WordCloud(
            font_path=font_path,
            width=800,
            height=400,
            background_color='white'
        ).generate(text)

        # 색 입히기
        wordcloud.recolor(color_func=snu_color_func)

        axes[i].imshow(wordcloud, interpolation='bilinear')
        axes[i].axis('off')
        axes[i].set_title(f"{area} 영역 WordCloud", fontsize=14)

    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    st.pyplot(fig)

# Streamlit 출력
st.subheader("공통교양 영역별 WordCloud")
generate_wordcloud_by_area(df, font_path=korean_font)   

st.markdown(f"""
<div style='font-size:100%; color:#333; line-height:1.6;'>
    <p>
        흥미로운 점은 이 베리타스 영역이 갖는 교육적 무게감은 단순한 수치에 비해 훨씬 크다는 사실이다.
        서울대학교 단과대학별 이수 규정을 정리해보면, 평균적으로 '학문의 토대' 영역에서 25.7학점을 이수해야 하는 데 반해,
        베리타스는 평균 3.1학점으로 가장 적은 수치를 기록한다.
        하지만 대부분의 단과대학에서 베리타스를 '선택'이 아닌 '필수'로 규정하고 있다는 점은,
        이 영역이 단지 수업량으로 평가할 수 없는 교육적 함의를 가진다는 점을 시사한다.
    </p>
    </div>
""", unsafe_allow_html=True)

# 이수 규정 그래프 넣기

# CSV 파일 불러오기
df = pd.read_csv('CourseRequirement.csv')

# 분석 대상 영역
area_cols = ['지성의 열쇠', '지성의 확장', '학문의 토대', '베리타스']

# 평균 이수학점 계산
area_means = df[area_cols].mean().sort_values(ascending=False).reset_index()
area_means.columns = ['공통교육 영역', '평균 이수학점']
st.write(area_means)

snu_colors = {
    '학문의 토대': '#666666',   # snu_gray
    '지성의 열쇠': '#0f0f70',   # snu_blue
    '지성의 확장': '#8b6f4d',   # snu_gold
    '베리타스': '#dcdab2'      # snu_beige
}

# Altair 차트
bar_chart = alt.Chart(area_means).mark_bar().encode(
    x=alt.X('공통교육 영역:N', sort='-y', title='공통교육 영역'),
    y=alt.Y('평균 이수학점:Q', title='평균 이수학점'),
    color=alt.Color('공통교육 영역:N',
                    scale=alt.Scale(domain=list(snu_colors.keys()), range=list(snu_colors.values())),
                    legend=None),    
    tooltip=['공통교육 영역', '평균 이수학점']
).properties(
    width=600,
    height=400,
    title='공통교육 영역별 평균 이수학점'
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_title(
    fontSize=18,
    anchor='start'
)

# Streamlit에 출력
st.subheader('단과대학별 공통교육 영역 평균 이수학점')
st.altair_chart(bar_chart, use_container_width=True)
            

st.markdown(f"""
<div style='font-size:100%; color:#333; line-height:1.6;'>
    <p>
        이는 베리타스가 지닌 성격, 즉 철학적 성찰과 윤리적 실천을 요구하는 수업이
        다른 영역에 비해 개설이나 수강이 더 어렵고 까다롭기 때문이기도 하다.
        실제로 베리타스 과목은 단과대학 고유의 전공 지식이나 학문 분야와는 일정한 거리를 유지한다.
        이 영역은 오히려 다양한 전공과 배경을 가진 학생들이 함께 공통된 질문을 탐색하고,
        공동체의 일원으로서의 책임감을 학습하는 데 초점을 맞춘다.
    </p>
    <p>
        다시 말해, 베리타스는 교양 교육의 '내용'을 풍성하게 하기보다,
        교양 교육의 '방향'을 명확히 설정하는 장치에 가깝다.
        따라서 과목 수나 이수학점만으로 이 영역의 중요도를 판단하는 것은 곤란하다.
    </p>
    <p>
        그렇다고 해서 베리타스가 현재 상태로 충분하다고 보기는 어렵다.
        지금의 교양 교육과정은 여전히 '학문의 토대'에 무게가 쏠려 있으며,
        '지성의 열쇠'와 '지성의 확장'이 그 균형을 일부 보완하고 있는 구조다.
        베리타스는 이런 구조의 바깥에 존재한다.
        그 수업의 성격상 대규모로 개설하거나 다양한 전공 교수들이 개입하기 어렵기 때문에,
        교과목 수나 이수 학점 확대에 있어 현실적인 제약이 뒤따른다.
    </p>
    <p>
        그러나 그렇기에 더욱 베리타스는 현재 구조를 유지한 채 내실화되어야 하며,
        장기적으로는 다른 세 영역이 베리타스의 방향성을 일부 수용해 교양 교육 전체의 재편으로 이어질 필요가 있다.
        결국 서울대학교가 추구하는 교양 교육은 단순히 다양한 지식을 습득하는 데 그치지 않고,
        그 지식이 어떤 사회적 맥락 속에서 작동하며,
        개인이 그 속에서 어떤 역할과 책임을 가져야 하는지를 함께 사유하는 방식으로 이동하고 있다.
    </p>
    <p>
        베리타스는 그 움직임의 핵심적 징후다. 아직 작고 낯설지만, 가장 분명한 방향을 보여주는 영역.
        그것이 지금 서울대 교양 교육의 베리타스다. <br>
    </p>
</div>
""", unsafe_allow_html=True)









st.markdown("---")
st.subheader('서울대인의 목소리')
user_opinion = st.text_input('당신이 생각하는 융합교육이란 무엇인가요?')

# SNU 컬러 팔레트
snu_palette = ['rgb(15, 15, 112)',
               'rgb(220, 218, 178)',
               'rgb(102, 102, 102)',
               'rgb(139,111,77)',
               'rgb(139,141,143)']

def snu_color_func(word, font_size, position, orientation, font_path, random_state):
    return random.choice(snu_palette)

# CSV 경로 지정
csv_path = "opinions.csv"

# CSV 불러오기 또는 새로 만들기
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=['opinion'])

# 사용자 입력 처리
if user_opinion:
    new_row = pd.DataFrame([[user_opinion]], columns=['opinion'])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(csv_path, index=False)

# 워드클라우드 생성 및 표시
if not df.empty:
    text = ' '.join(df['opinion'].dropna().astype(str))
    wordcloud = WordCloud(
        font_path='NotoSansKR-Bold.ttf',
        width=800,
        height=400,
        background_color='white'
    ).generate(text)

    wordcloud.recolor(color_func=snu_color_func)  # 🎨 색상 입히기

    st.subheader("융합교육에 대한 서울대인의 생각")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)

