import streamlit as st
import pickle


knn_model=pickle.load(open('KNNModel.pkl','rb'))

def predict_note_authentication(radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave points_worst,symmetry_worst,fractal_dimension_worst):
    
    prediction=knn_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave points_worst,symmetry_worst,fractal_dimension_worst]])
    print(prediction)
    return prediction

def main():
    st.title("Streamlit Tutorial")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Tumor Analysis</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
   
   radius_mean = st.text_input("radius_mean","Type Here")
    texture_mean = st.text_input("texture_mean","Type Here")
    perimeter_mean = st.text_input("perimeter_mean","Type Here")
    area_mean = st.text_input("area_mean","Type Here")
    smoothness_mean = st.text_input("smoothness_mean","Type Here")
    compactness_mean = st.text_input("compactness_mean","Type Here")
    concavity_mean = st.text_input("concavity_mean","Type Here")
    concave points_mean = st.text_input("concave points_mean","Type Here")
    symmetry_mean = st.text_input("symmetry_mean","Type Here")
    fractal_dimension_mean = st.text_input("fractal_dimension_mean","Type Here")
    radius_se = st.text_input("radius_se","Type Here")
    texture_se = st.text_input("texture_se","Type Here")
    perimeter_se = st.text_input("perimeter_se","Type Here")
    area_se = st.text_input("area_se","Type Here")
    smoothness_se = st.text_input("smoothness_se","Type Here")
    compactness_se = st.text_input("compactness_se","Type Here")
    concavity_se = st.text_input("concavity_se","Type Here")
    concave points_se = st.text_input("concave points_se","Type Here")
    symmetry_se = st.text_input("symmetry_se","Type Here")
    fractal_dimension_se = st.text_input("fractal_dimension_se","Type Here")
    radius_worst = st.text_input("radius_worst","Type Here")
    texture_worst = st.text_input("texture_worst","Type Here")
    perimeter_worst = st.text_input("perimeter_worst","Type Here")
    area_worst = st.text_input("area_worst","Type Here")
    smoothness_worst = st.text_input("smoothness_worst","Type Here")
    compactness_worst = st.text_input("compactness_worst","Type Here")
    concavity_worst = st.text_input("concavity_worst","Type Here")
    concave points_worst = st.text_input("concave points_worst","Type Here")
    symmetry_worst = st.text_input("symmetry_worst","Type Here")
    fractal_dimension_worst = st.text_input("fractal_dimension_worst","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave points_worst,symmetry_worst,fractal_dimension_worst)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()

    
    																													
        
    
    
    
    
