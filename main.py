import streamlit as st

# 1. 세션 상태 초기화
if 'posts' not in st.session_state:
    st.session_state.posts = []

if 'edit_index' not in st.session_state:
    st.session_state.edit_index = None

# 2. 사이드바 메뉴 구성
menu_option = st.sidebar.radio("메뉴 선택", ["글 목록", "글 작성"])

# 3. 글 작성 화면
if menu_option == "글 작성":
    st.header("새 글 작성")
    title = st.text_input("제목")
    content = st.text_area("내용")
    
    if st.button("등록하기"):
        if title and content:
            new_post = {"title": title, "content": content}
            st.session_state.posts.append(new_post)
            st.success("글이 성공적으로 등록되었습니다!")
        else:
            st.error("제목과 내용을 모두 입력해주세요.")

# 4. 글 목록 및 편집 화면
elif menu_option == "글 목록":
    
    # 편집 모드인 경우
    if st.session_state.edit_index is not None:
        idx = st.session_state.edit_index
        st.header("글 편집")
        # 편집 폼: 기존 제목과 내용을 기본값으로 사용
        edited_title = st.text_input("제목", value=st.session_state.posts[idx]["title"], key="edit_title")
        edited_content = st.text_area("내용", value=st.session_state.posts[idx]["content"], key="edit_content")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("저장"):
                st.session_state.posts[idx]["title"] = st.session_state.edit_title
                st.session_state.posts[idx]["content"] = st.session_state.edit_content
                st.success("글이 수정되었습니다!")
                st.session_state.edit_index = None  # 편집 모드 종료
        with col2:
            if st.button("취소"):
                st.session_state.edit_index = None  # 편집 모드 취소
        st.markdown("---")
    
    st.header("글 목록")
    if st.session_state.posts:
        # 최신 글이 상단에 오도록 역순으로 출력
        for i, post in enumerate(st.session_state.posts[::-1]):
            # 원래 리스트의 인덱스 계산
            original_index = len(st.session_state.posts) - 1 - i
            with st.expander(f"{post['title']}"):
                st.write(post["content"])
                # 편집 버튼: 클릭하면 해당 게시글의 인덱스를 저장해 편집 모드로 전환
                if st.button("편집", key=f"edit_{original_index}"):
                    st.session_state.edit_index = original_index
    else:
        st.info("등록된 글이 없습니다.")
