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
import plotly.express as px
import matplotlib.font_manager as fm



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

tab1, tab2, tab3, tab4 = st.tabs(['학부대학', '서울대 학부대학 비전', '서울대 학부대학 교과목', '서울대 학부대학 비교과'])

with tab1:
    st.header('학부대학이란 무엇인가?')
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


#    program_img_path = college_data['program_img_path']
#    st.image(program_img_path, width = 300)
#    st.markdown(college_data['program_text'])
    

    




with tab2:
    st.header('서울대 학부대학의 비전은 무엇인가?')
    st.markdown(f"""
    <div style='font-size:100%; color:#333; line-height:1.6;'>
        <p>
            서울대학교 학부대학은 2025년 3월, 관악캠퍼스 종합화 50주년을 기념하며 출범한 새로운 교육 조직으로, 
            서울대 학부교육 혁신의 전면에 나서고자 한다. “도전과 공감으로 미래를 여는 지성”이라는 인재상을 바탕으로, 
            학문 간 경계를 넘는 융합적 사고와 학생 주도의 학습 설계를 지원하는 플랫폼으로 기능한다.
        </p>
        <p>
            학부대학의 비전은 단순한 교과 개편을 넘어, 교육 구조 자체를 재설계하려는 데 있다. 
            무전공 입학 확대, 공통교양 강화, 마이크로디그리 도입 등은 제도 변화 그 이상으로, 
            학생의 주체성과 사회적 책임감을 함께 기르는 교육 철학을 반영한다.
        </p>
        <p>
            공통핵심역량과 융합 교육의 내실화를 통해, 단일 학문을 넘는 통합적 사고와 실천적 역량을 강조하며, 
            비교과 프로그램 혁신과 현장 중심 학습도 강화하고 있다. 
            더불어 복수전공, 학생설계전공, 연합·연계 전공 등 유연한 전공 설계를 행정적으로 지원하며, 
            학과 중심의 고정된 틀에서 벗어난 학사 구조로의 전환을 주도한다.
        </p>
        <p>
            궁극적으로 학부대학은 학생이 스스로 미래를 설계할 수 있는 열린 교육 생태계를 지향한다. 
            공급 중심에서 수요 중심으로 이동하는 시대에, 
            학부대학은 서울대 교육 혁신의 사상적·제도적 구심점으로 자리하고 있다.
        </p>
        </div>
    """, unsafe_allow_html=True)

    st.image('./core_skills_img.png')        





with tab3:
    st.header('서울대 학부대학 교양교육과정은?')
    ## 본론 2: 서울대 학부대학_교양교육과정
    st.markdown(f"""
    <div style='font-size:100%; color:#333; line-height:1.6;'>
        <p>
            2025학년도부터 서울대학교 학부대학은 공통교양 교육과정을 전면 개편했다. 
            이번 개편은 단순한 과목 조정이 아니라, 교양 교육의 철학과 방향성을 새롭게 설정한 선언에 가깝다. 
            학문 수행을 위한 기초 역량부터 인간과 사회에 대한 이해, 공적 책임에 대한 성찰까지, 
            서울대는 교양 교육을 통해 무엇을 가르칠 것인지 근본적으로 되묻고 있다. 
            이 가운데 가장 주목할 변화는 ‘베리타스(Veritas)’ 영역의 신설이다.
        </p>
        <p>
            기존 공통교양은 ‘학문의 토대’, ‘지성의 열쇠’, ‘지성의 확장’ 세 영역으로 구성되어 있었다. 
            ‘학문의 토대’는 글쓰기, 외국어, 수학·과학 등 기초 도구 역량을, 
            ‘지성의 열쇠’는 역사·철학·문화 해석 등 인문학적 탐구를, 
            ‘지성의 확장’은 자기주도적 학습과 창의적 사고를 중심에 둔다. 
            여기에 새로 추가된 ‘베리타스’는 공동체적 가치와 실천 윤리를 중심으로 설계되어, 
            서울대가 지향하는 교양 인재상에 방향성을 부여한다.
        </p>
        <p>
            이 개편은 학부대학의 출범과 맞물려 더욱 주목된다. 학부대학은 단순한 행정 조직이 아니라, 
            서울대가 추구하는 학부교육의 비전을 설계하고 실현하는 플랫폼이다. 
            무전공 입학, 마이크로디그리, 공통교양 강화 등은 학생 주도의 전공 설계와 학문 탐색을 지원하는 구조로 설계되었으며, 
            베리타스는 그 교양 교육의 핵심 축으로 기능한다.
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
        fontSize=16,
        anchor='start'
    )

    # 출력
    st.altair_chart(bar_chart, use_container_width=True)
    st.caption("※ 데이터 기준: 2025학년도 1학기 기초교양 수강편람")


    ## wordcloud
    # 데이터 불러오기
    df = pd.read_csv('CourseList.csv')
    korean_font = './NotoSansKR-Bold.ttf'

    # SNU 컬러 팔레트
    snu_palette = ['rgb(15, 15, 112)',
                'rgb(220, 218, 178)',
                'rgb(102, 102, 102)',
                'rgb(139,111,77)',
                'rgb(139,141,143)']

    # 폰트 객체 생성
    font_path1 = './NotoSansKR-Medium.ttf'  # 원하는 한글 폰트 경로
    fontprop = fm.FontProperties(fname=font_path1)

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
            axes[i].set_title(f"{area}", fontsize=16, fontproperties=fontprop)

        for j in range(i + 1, len(axes)):
            axes[j].axis('off')

        plt.tight_layout()
        st.pyplot(fig)

    # Streamlit 출력
    generate_wordcloud_by_area(df, font_path=korean_font)   

    st.markdown(f"""
    <div style='font-size:100%; color:#333; line-height:1.6;'>
        <p>
            실제로 WordCloud 분석에서도 베리타스 영역은 다른 영역에 비해 상대적으로 적은 수의 키워드만이 시각적으로 나타난다.
            이는 과목 수의 부족뿐 아니라, 베리타스 교과목이 특정 분야나 전공 지식보다는 가치 중심적 내용으로 구성되어 있어
            텍스트 기반의 키워드 추출에서도 비교적 약하게 드러나기 때문이다.
        </p>
        </div>
    """, unsafe_allow_html=True)



    ## 공통교육 영역별 평균 이수학점 막대그래프
    # CSV 파일 불러오기
    df = pd.read_csv('CourseRequirement.csv')

    # 분석 대상 영역
    area_cols = ['지성의 열쇠', '지성의 확장', '학문의 토대', '베리타스']

    # 평균 이수학점 계산
    area_means = df[area_cols].mean().sort_values(ascending=False).reset_index()
    area_means.columns = ['공통교육 영역', '평균 이수학점']

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
        fontSize=16,
        anchor='start'
    )

    # Streamlit에 출력
    st.markdown("""
    <br><br><br><br><br><br>
    """, unsafe_allow_html=True)
    st.subheader('단과대학별 공통교육 영역 평균 이수학점')
    st.altair_chart(bar_chart, use_container_width=True)


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


    ## 단과대별 베리타스 요구 비율과 최소 교양 이수 학점 산점도
    df1 = pd.read_csv('CourseRequirements_mean.csv')
    # x축: 베리타스 비율
    df1['베리타스_비율'] = df1['베리타스'] / df1['최소 학점']

    # y축: 최소학점
    df1['최소학점'] = df1['최소 학점']

    # 색상 그룹핑
    def group_dept(name):
        for keyword in ['학부대학', '인문', '사회과학', '자연과학', '간호', '경영', '공과', '농업', 
                        '미술', '사범', '생활', '수의', '약학', '음악', '의과', '첨단', '치의학']:
            if keyword in name:
                return keyword
        return '기타'

    df1['대학그룹'] = df1['대학'].apply(group_dept)

    # Plotly 산점도
    fig = px.scatter(
        df1,
        x='베리타스_비율',
        y='최소학점',
        color='대학그룹',
        hover_name='대학',
        title='단과대별 베리타스 요구 비율과 최소 교양 이수 학점'
    )

    fig.update_layout(
    xaxis_title='전체 중 베리타스 요구 비율',
    yaxis_title='전체 교양 이수 학점'
    )   

    fig.update_layout(
        xaxis=dict(range=[0, 0.2], title='베리타스 요구 비율'),
        yaxis=dict(range=[30, 60], title='최소 교양 이수 학점')
    )

    # Streamlit에서 출력
    st.plotly_chart(fig, use_container_width=True)



    ## 단과대별 공통교양 영역별 이수 학점 누적 막대그래프
    # 시각화 대상 열
    cols = ['학문의 토대', '지성의 열쇠', '베리타스', '지성의 확장']
    stacked_data = df1[['대학'] + cols].copy()

    # long-form 데이터로 변환
    stacked_melted = stacked_data.melt(id_vars='대학', value_vars=cols,
                                    var_name='영역', value_name='과목 수')

    # 색상 지정
    color_map = {
        '학문의 토대': '#666666',   # snu_gray
        '지성의 열쇠': '#0f0f70',   # snu_blue
        '지성의 확장': '#8b6f4d',   # snu_gold
        '베리타스': '#dcdab2'      # snu_beige
    }

    # Plotly 누적 막대그래프 생성
    fig = px.bar(
        stacked_melted,
        x='대학',
        y='과목 수',
        color='영역',
        color_discrete_map=color_map,
        title='단과대별 공통교양 영역별 이수 학점'
    )

    fig.update_layout(
        barmode='stack',
        xaxis_tickangle=-45,
       yaxis_title='학점 수'
    )

    # Streamlit 출력
    st.plotly_chart(fig, use_container_width=True)



    st.markdown(f"""
    <div style='font-size:100%; color:#333; line-height:1.6;'>
        <p>
            베리타스 과목은 단과대학의 전공 지식과는 일정한 거리를 둔다. 
            이 영역은 다양한 전공의 학생들이 공통된 질문을 탐색하고, 공동체의 책임을 학습하는 데 초점을 맞춘다. 
            교양 교육의 ‘내용’을 보완하기보다, 그 ‘방향’을 제시하는 장치에 가깝기 때문에, 
            단순히 과목 수나 학점 기준으로 중요도를 판단하기 어렵다.
        </p>
        <p>
            하지만 현재 베리타스의 구성은 충분하다고 보기 어렵다. 교양 교육은 여전히 ‘학문의 토대’ 중심이며, 
            ‘지성의 열쇠’와 ‘지성의 확장’이 그 균형을 일부 보완하는 구조다. 베리타스는 그 바깥에 존재하며, 
            수업 특성상 대규모 개설이나 다양한 전공 교수의 참여가 어렵다. 따라서 당장 과목 수를 확대하기보다는 현재 구조 안에서 내실을 다지고, 
            장기적으로 다른 영역이 베리타스의 철학을 일부 수용해 교양 교육의 방향을 함께 재편할 필요가 있다.
        </p>
        <p>
            서울대가 지향하는 교양 교육은 지식의 습득을 넘어, 그것이 사회적 맥락 속에서 어떤 역할을 하며, 
            개인이 어떤 책임을 져야 하는지를 성찰하는 방식으로 나아가고 있다. 베리타스는 이 전환을 가장 분명하게 드러내는 징후다. 
            아직은 작고 낯설지만, 가장 선명한 방향을 가리키고 있다. <br>
        </p>
    </div>
    """, unsafe_allow_html=True)















with tab4:
    st.header('서울대 학부대학 비교과')
    st.image('https://static.streamlit.io/examples/owl.jpg')


st.markdown("---" "---")













st.markdown("""
<div style='background-color:#0f0f70; padding: 15px 30px; border-radius: 10px; margin-bottom: 20px;'>
    <h3 style='color: white; text-align: center;'>융합교육에 대한 서울대인의 생각</h3>
</div>
""", unsafe_allow_html=True)

# 입력창 - 라벨 제거, 플레이스홀더만
user_opinion = st.text_input("", placeholder="당신이 생각하는 융합교육이란 무엇인가요?")


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

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)