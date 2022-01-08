import streamlit as st
import.streamlit.components.v1 as stc



#Load EDA



def main():
    st.title("Aplikacija za ponudu tečaja by Josip Požega, prof.")

    menu=["Početna", "Preporuke,", "O aplikaciji"]
    choice= st.sidebar.selectbox("Izbornik", menu)


    if choice == "Početna":
        st.subheader("Početna")
    elif chice == "Preporuke":
        st.subheader == "Preporuka tečajeva":
    else:
        st.subheader("O aplikaciji")
        st.text("Aplikacija by Josip Požega, prof.")
        st.text("Napravljeno sa Streamlitom & Pandom")





if __name__ == __'main__':
    main()
