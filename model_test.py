import os
import joblib
import pandas as pd

# Current project folder
current_folder = os.path.dirname(__file__)

# Dataset path
train_path = os.path.join(current_folder, "dataset", "KDDTrain+.txt")

# Model path
model_path = os.path.join(current_folder, "model", "cyber_threat_model.pkl")

# Load dataset
column_names = [
'duration','protocol_type','service','flag','src_bytes','dst_bytes','land',
'wrong_fragment','urgent','hot','num_failed_logins','logged_in',
'num_compromised','root_shell','su_attempted','num_root',
'num_file_creations','num_shells','num_access_files',
'num_outbound_cmds','is_host_login','is_guest_login','count',
'srv_count','serror_rate','srv_serror_rate','rerror_rate',
'srv_rerror_rate','same_srv_rate','diff_srv_rate',
'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
'dst_host_same_srv_rate','dst_host_diff_srv_rate',
'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
'dst_host_serror_rate','dst_host_srv_serror_rate',
'dst_host_rerror_rate','dst_host_srv_rerror_rate',
'label','difficulty'
]

train = pd.read_csv(train_path, names=column_names)

print("✅ Dataset Loaded Successfully!")
print("Rows:", train.shape[0])
print("Columns:", train.shape[1])

# Load model
model = joblib.load(model_path)

print("✅ Model Loaded Successfully!")
from sklearn.preprocessing import LabelEncoder

# Create LabelEncoder
encoder = LabelEncoder()

# Convert text columns into numbers
train['protocol_type'] = encoder.fit_transform(train['protocol_type'])
train['service'] = encoder.fit_transform(train['service'])
train['flag'] = encoder.fit_transform(train['flag'])
train['label'] = encoder.fit_transform(train['label'])

print("✅ Text columns converted into numbers successfully!")

# Separate features and target
X = train.drop('label', axis=1)
y = train['label']

print("Features shape:", X.shape)
print("Target shape:", y.shape)
from sklearn.model_selection import train_test_split

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("✅ Data split successfully!")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))
# Make prediction using the saved model
prediction = model.predict(X_test)

print("✅ Prediction completed successfully!")
print("First 10 Predictions:")
print(prediction[:10])