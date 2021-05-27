import joblib
model = joblib.load('salary_prediction.pk1')

y_pred=float(input("Enter Year of Experience: " ))

print("Predicted Salary is: ",model.predict([[y_pred]]))