import csv
import math
import random
from sklearn.model_selection import train_test_split

# Đọc dữ liệu từ tệp train.csv
train_data = []
with open("Code\\Final\\data_train.csv", 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        train_data.append(line)

# Đọc dữ liệu từ tệp test.csv
test_data = []
with open("Code\\Final\\data_test.csv", 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        test_data.append(line)


class Diabetes:
    def __init__(self):
        self.total_samples = 0
        self.true_feature_counts = {}
        self.false_feature_counts = {}
        self.true_word_counts = {}
        self.false_word_counts = {}

    def calculate_feature_count(self, outcome, pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi,
                                diabetes_pedigree_function, age):
        self.total_samples += 1

        # Count the occurrences of features for each outcome
        self.increment_feature_count(
            outcome, pregnancies, self.true_feature_counts, self.false_feature_counts)
        self.increment_feature_count(
            outcome, glucose, self.true_feature_counts, self.false_feature_counts)
        self.increment_feature_count(
            outcome, blood_pressure, self.true_feature_counts, self.false_feature_counts)
        self.increment_feature_count(
            outcome, skin_thickness, self.true_feature_counts, self.false_feature_counts)
        self.increment_feature_count(
            outcome, insulin, self.true_feature_counts, self.false_feature_counts)
        self.increment_feature_count(
            outcome, bmi, self.true_feature_counts, self.false_feature_counts)
        self.increment_feature_count(
            outcome, diabetes_pedigree_function, self.true_feature_counts, self.false_feature_counts)
        self.increment_feature_count(
            outcome, age, self.true_feature_counts, self.false_feature_counts)

        # Count the occurrences of words for each outcome
        words = outcome.split(" ")
        for word in words:
            if outcome == "1":
                self.true_word_counts[word] = self.true_word_counts.get(
                    word, 0) + 1
            else:
                self.false_word_counts[word] = self.false_word_counts.get(
                    word, 0) + 1

    def classify(self, pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age):
        true_probability = self.calculate_outcome_probability("1", pregnancies, glucose, blood_pressure, skin_thickness,
                                                              insulin, bmi, diabetes_pedigree_function, age)
        false_probability = self.calculate_outcome_probability("0", pregnancies, glucose, blood_pressure, skin_thickness,
                                                               insulin, bmi, diabetes_pedigree_function, age)

        if true_probability > false_probability:
            return "1"
        else:
            return "0"

    def calculate_outcome_probability(self, outcome, pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi,
                                      diabetes_pedigree_function, age):
        probability = 1.0

        # Calculate probability based on features
        probability *= self.get_feature_count(outcome,
                                              pregnancies) / self.total_samples
        probability *= self.get_feature_count(outcome,
                                              glucose) / self.total_samples
        probability *= self.get_feature_count(outcome,
                                              blood_pressure) / self.total_samples
        probability *= self.get_feature_count(outcome,
                                              skin_thickness) / self.total_samples
        probability *= self.get_feature_count(outcome,
                                              insulin) / self.total_samples
        probability *= self.get_feature_count(outcome,
                                              bmi) / self.total_samples
        probability *= self.get_feature_count(outcome,
                                              diabetes_pedigree_function) / self.total_samples
        probability *= self.get_feature_count(outcome,
                                              age) / self.total_samples

        # Calculate probability based on words
        words = outcome.split(" ")
        for word in words:
            if outcome == "1":
                probability *= (self.true_word_counts.get(word, 0) + 1) / \
                    (self.total_samples + len(self.true_word_counts))
            else:
                probability *= (self.false_word_counts.get(word, 0) + 1) / \
                    (self.total_samples + len(self.false_word_counts))

        return probability

    def increment_feature_count(self, outcome, feature, true_counts, false_counts):
        if outcome == "1":
            true_counts[feature] = true_counts.get(feature, 0) + 1
        else:
            false_counts[feature] = false_counts.get(feature, 0) + 1

    def get_feature_count(self, outcome, feature):
        return self.true_feature_counts.get(feature, 0) if outcome == "1" else self.false_feature_counts.get(feature, 0)

    def train(self, dataset):
        classifier = Diabetes()
        for line in dataset:
            outcome = line[8]
            pregnancies = line[0]
            glucose = line[1]
            blood_pressure = line[2]
            skin_thickness = line[3]
            insulin = line[4]
            bmi = line[5]
            diabetes_pedigree_function = line[6]
            age = line[7]
            classifier.calculate_feature_count(outcome, pregnancies, glucose, blood_pressure, skin_thickness,
                                               insulin, bmi, diabetes_pedigree_function, age)
        return classifier

    def test(self, train_data, test_data):
        classifier = self.train(train_data)
        correct_predictions = 0
        total_test_samples = 0
        true_positives = 0
        false_positives = 0
        true_negatives = 0
        false_negatives = 0

        for test_line in test_data:
            true_outcome = test_line[8]
            test_pregnancies = test_line[0]
            test_glucose = test_line[1]
            test_blood_pressure = test_line[2]
            test_skin_thickness = test_line[3]
            test_insulin = test_line[4]
            test_bmi = test_line[5]
            test_diabetes_pedigree_function = test_line[6]
            test_age = test_line[7]

            predicted_outcome = classifier.classify(test_pregnancies, test_glucose, test_blood_pressure,
                                                    test_skin_thickness, test_insulin, test_bmi,
                                                    test_diabetes_pedigree_function, test_age)
            if predicted_outcome == true_outcome:
                correct_predictions += 1
                if true_outcome == "1":
                    true_positives += 1
                if true_outcome == "0":
                    true_negatives += 1
            else:
                if predicted_outcome == "1":
                    false_positives += 1
                if predicted_outcome == "0":
                    false_negatives += 1
            total_test_samples += 1

        if true_positives + false_positives > 0:
            precision = true_positives / (true_positives + false_positives)
        else:
            precision = 0

        recall = true_positives / (true_positives + false_negatives)
        if precision + recall > 0:
            f1_score = 2 * (precision * recall) / (precision + recall)
        else:
            f1_score = 0

        print(true_outcome)

        print("Precision:", precision)
        print("Recall:", recall)
        print("F1 Score:", f1_score)

        print("Correct Prediction:", correct_predictions)
        print("Total Prediction:", total_test_samples)
        print("Accuracy:", correct_predictions / total_test_samples)

    def predict(self, pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age):
        model = self.train(train_data)
        result = model.classify(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi,
                                diabetes_pedigree_function, age)
        return result


if __name__ == "__main__":
    diabetes_classifier = Diabetes()
    diabetes_classifier.test(train_data, test_data)
