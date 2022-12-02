import streamlit as st
from RC5 import RC5


st.title('Шифр RC5')
st.write("Описание из Википедии [RC5](https://ru.wikipedia.org/wiki/RC5)")


with st.sidebar:
    bite = st.selectbox("Длина слова в битах: ", (16, 32, 64))
    number = st.number_input('Количество раундов:', 1, 255)
    keys = st.text_input('Ключ', 'Key')


col1, col2 = st.columns(2)

with col1:
    st.subheader('Зашифровать слово')
    string = ""
    text = st.text_input('Слово', 'Hello world')
    if st.button('Зашифровать'):
        try:
            rc5 = RC5(keys.encode(), bite, number)
            encryptText = rc5.encrypt(text.encode('utf-8'))
            string += "{}".format(b''.join(encryptText).hex())
            st.markdown(f"Зашифрованное слово: {string}")
        except ValueError:
            st.markdown(f"Ошибка, попробуйте снова")

with col2:
    st.subheader('Расшифровать слово')
    string = ""
    text = st.text_input('Зашифрованное слово', '')
    if st.button('Расшифровать'):
        try:
            rc5 = RC5(keys.encode(), bite, number)
            decryptText = rc5.decrypt(bytes.fromhex(text))
            utf8String = str(b''.join(decryptText), 'utf-8')
            string += "{}\n".format(utf8String)
            st.markdown(f"Расшифрованное слово: {string}")
        except ValueError:
            st.markdown(f"Ошибка, попробуйте снова")

