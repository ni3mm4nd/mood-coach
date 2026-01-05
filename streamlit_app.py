import streamlit as st

st.title("Mood Coach")
st.write("Ahoj! Uděláme mini aplikaci na doporučení podle nálady.")

name = st.text_input("Jak se jmenuješ?")
mood = st.slider("Jaká je tvoje nálada? (0 = špatná, 10 = super)", 0, 10, 5)

st.write("Jméno:", name)
st.write("Nálada:", mood)

if mood <= 3:
    st.warning("Dnes to nevypadá moc dobře. Zkus něco jednoduchého a odpočinek.")
elif mood <= 7:
    st.info("Jde to! Zkus krátkou procházku nebo něco kreativního.")
else:
    st.success("Super! Využij energii na něco těžšího nebo sport.")

st.subheader("Co máš dnes chuť dělat?")
sport = st.checkbox("Sport")
games = st.checkbox("Hry")
music = st.checkbox("Hudba")
friends = st.checkbox("Kamarádi")

score = 0
if sport: score += 2
if friends: score += 2
if music: score += 1
if games: score += 1

st.write("Tvoje aktivní skóre:", score)

if st.button("Doporuč mi program"):
    st.write(f"Ok, {name if name else 'kamaráde'}!")
    if mood <= 3:
        st.write("1) Napij se vody  2) 5 minut protažení  3) krátká pauza od displeje")
    elif mood <= 7:
        st.write("1) 10 minut procházka  2) hudba  3) udělej jednu malou věc do školy")
    else:
        st.write("1) Sport / trénink  2) nauč se něco nového  3) pomoz někomu doma")
