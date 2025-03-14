import streamlit as st
import joblib
import pandas as pd

# 加载训练好的模型
model = joblib.load("student_score_model.pkl")

# 创建 Streamlit 界面
st.title("🎓 学生成绩预测系统")
st.write("输入学生信息，预测最终成绩 G3")

# 创建输入框
G1 = st.number_input("G1 (第一学期成绩)", min_value=0, max_value=20, value=10)
G2 = st.number_input("G2 (第二学期成绩)", min_value=0, max_value=20, value=10)
absences = st.number_input("absences (缺勤次数)", min_value=0, max_value=100, value=5)
age = st.number_input("age (年龄)", min_value=15, max_value=22, value=18)
romantic = st.selectbox("是否有恋爱关系", ["否", "是"])
famrel = st.slider("家庭关系质量 (1-5)", min_value=1, max_value=5, value=3)

# 处理输入数据
romantic = 1 if romantic == "是" else 0
input_data = pd.DataFrame([[G2, absences, G1, age, romantic, famrel]],
                          columns=["G2", "absences", "G1", "age", "romantic", "famrel"])

# 预测按钮
if st.button("预测成绩"):
    prediction = model.predict(input_data)
    st.success(f"📊 预测的最终成绩 (G3): {round(prediction[0], 2)}")

