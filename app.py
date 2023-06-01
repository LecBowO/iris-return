import streamlit as st
import pickle
import sklearn

st.set_page_config(page_title='IRIS | PRIDICTOR', page_icon='images/favicon.png')

st.title("IRIS FLOWER PRIDICTOR")
st.image("images/main-iris.png", width=280)

target = ['setosa', 'versicolor', 'virginica']

model = pickle.load(open('model.pkl', 'rb'))

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    sepal_length = st.number_input("Enter Sepal Length")
with col2:
    sepal_width = st.number_input("Enter Sepal Width")
with col3:
    petal_length = st.number_input("Enter Petal Length")
with col4:
    petal_width = st.number_input("Enter Petal Width")

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction == 0:
        prediction = "Sentosa"
        st.image("images/sentosa.png", width=225)
        st.text("Iris setosa has a deep violet blue flower. The sepals are deeply-veined dark purple ")
        st.text("with a yellow-white signal. The petals are very reduced in size, not exceeding the ")
        st.text("base of the sepals. Beachhead iris flowers in late spring, on a one ")
        st.text("flowered inflorescence.")
    elif prediction == 1:
        prediction = "Versicolor"
        st.image("images/versicolor.png", width=225)
        st.text("Iris versicolor is a flowering herbaceous perennial plant, growing 10–80 cm (4–31 in) high. ")
        st.text("It tends to form large clumps from thick, creeping rhizomes. ")
        st.text("The unwinged, erect stems generally have basal leaves that are more than 1 cm (1⁄2 in) wide. Leaves are folded on the midribs so that they form an overlapping flat fan. The well developed blue flower has 6 petals and sepals spread out nearly flat and have two forms. The longer sepals are hairless and have a greenish-yellow blotch at their base. The inferior ovary is bluntly angled. Flowers are usually light to deep blue (purple and violet are not uncommon) and bloom during May to July. Fruit is a 3-celled, bluntly angled capsule. The large seeds can be observed floating in fall.")
    else:   
        prediction = 'Virginica'
        st.image("images/virginica.png", width=225)
        st.text("virginica has a light blue to deep violet, rarely white, flower. The sepals are spreading with darker blue to purple veins with a light yellow pubescent signal. Southern blue flag iris flowers in late spring. Flowers are a one- to two-flowered inflorescence on a barely- or non-branching stem.")

    st.subheader(prediction)