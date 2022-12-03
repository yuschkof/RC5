import streamlit as st
from RC5 import RC5


st.title('Шифр RC5')
st.write("Описание из Википедии [RC5](https://ru.wikipedia.org/wiki/RC5)")


with st.sidebar:
    bite = st.selectbox("Длина слова в битах: ", (16, 32, 64))
    number = st.number_input('Количество раундов:', min_value=1, max_value=255)
    keys = st.text_input('Ключ', 'Key')


tab1, tab2 = st.tabs(["Зашифровать", "Расшифровать"])

with tab1:
    string = ""
    text = st.text_input('Слово', 'Hello world')
    if st.button('Зашифровать'):
        try:
            rc5 = RC5(keys.encode(), bite, number)
            encryptText = rc5.encrypt(text.encode('utf-8'))
            t = [text[i:i + rc5.blockSize * 2] for i in range(0, len(text), rc5.blockSize * 2)]
            for i, j in zip(t, encryptText):
                if len(i) < (rc5.blockSize * 2):
                    i += " " * (rc5.blockSize * 2 - len(i))
                string = "{}\t--> {}\n".format(i, j.hex())
                st.markdown(f"{string}")
            string += ">>\n>> encrypt: {}\n".format(b''.join(encryptText).hex())
            st.markdown(f"{text} --> {'{}'.format(b''.join(encryptText).hex())}")
        except ValueError:
            st.markdown(f"Ошибка, попробуйте снова")

with tab2:
    string = ""
    text = st.text_input('Зашифрованное слово', '')
    if st.button('Расшифровать'):
        try:
            rc5 = RC5(keys.encode(), bite, number)
            decryptText = rc5.decrypt(bytes.fromhex(text))
            utf8String = str(b''.join(decryptText), 'utf-8')
            b = [text[i:i + rc5.blockSize * 4] for i in range(0, len(text), rc5.blockSize * 2)]
            t = [utf8String[i:i + rc5.blockSize * 2] for i in range(0, len(utf8String), rc5.blockSize * 2)]
            for i, j in zip(b, t):
                if len(i) < (rc5.blockSize * 2):
                    i += " " * (rc5.blockSize * 2 - len(i))
                string = "{}\t--> {}\n".format(i, j)
                st.markdown(f"{string}")
            st.markdown(f"{text} --> {utf8String}")
        except ValueError:
            st.markdown(f"Ошибка, попробуйте снова")

