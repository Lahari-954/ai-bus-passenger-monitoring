from sklearn.tree import DecisionTreeClassifier


# Training data
# Passenger count is the input
X = [
    [5],
    [10],
    [20],
    [30],
    [35],
    [40],
    [45],
    [48],
    [50],
    [55],
    [60]
]


# Crowd level is the output
y = [
    "LOW",
    "LOW",
    "LOW",
    "LOW",
    "MODERATE",
    "MODERATE",
    "MODERATE",
    "MODERATE",
    "HIGH",
    "HIGH",
    "HIGH"
]


# Create Decision Tree model
model = DecisionTreeClassifier()


# Train the model
model.fit(X, y)


# Test prediction
passenger_count = 45

prediction = model.predict([[passenger_count]])


print("Passengers:", passenger_count)
print("Predicted Crowd Level:", prediction[0])