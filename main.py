import streamlit as st

# 1. 세션 상태에 게시글 목록 초기화 (앱이 재실행될 때마다 존재하는지 확인)
if 'posts' not in st.session_state:
    st.session_state.posts = []

# 2. 사이드바 메뉴 구성 - 사용자에게 "글 목록"과 "글 작성" 중 선택하게 함
menu_option = st.sidebar.radio("메뉴 선택", ["글 목록", "글 작성"])

# 3. 글 작성 화면
if menu_option == "글 작성":
    st.header("새 글 작성")
    # 제목과 내용을 입력받을 위젯 생성
    title = st.text_input("제목")
    content = st.text_area("내용")
    
    # 글 등록 버튼 클릭시
    if st.button("등록하기"):
        # 제목과 내용이 모두 입력되었는지 확인
        if title and content:
            # 새 글 정보를 사전 형태로 생성 후 세션 상태에 추가
            new_post = {"title": title, "content": content}
            st.session_state.posts.append(new_post)
            st.success("글이 성공적으로 등록되었습니다!")
        else:
            st.error("제목과 내용을 모두 입력해주세요.")

# 4. 글 목록 화면
elif menu_option == "글 목록":
    st.header("글 목록")
    # 게시글이 존재하면 목록 표시, 없으면 안내 메시지 출력
    if st.session_state.posts:
        # 목록을 최신글 순서로 보기 위해 역순으로 출력해도 좋습니다.
        for idx, post in enumerate(st.session_state.posts[::-1]):
            # expander 위젯을 사용해서 제목 클릭 시 상세 내용 표시
            with st.expander(f"{post['title']}"):
                st.write(post["content"])
    else:
        st.info("등록된 글이 없습니다.")
