local_ans = {
    "precision": (
        "Precision measures how many predicted positive cases were actually "
        "positive.\nFormula: TP / (TP + FP)"
    ),
    "recall": (
        "Recall measures how many actual positive cases the model correctly "
        "identified.\nFormula: TP / (TP + FN)"
    ),
    "f1 score": (
        "F1-score is the harmonic mean of precision and recall.\n"
        "Formula: 2 * (Precision * Recall) / (Precision + Recall)"
    ),
    "mae": (
        "MAE (Mean Absolute Error) is the average absolute difference "
        "between actual and predicted values.\n"
        "Formula: sum(abs(actual - predicted)) / number of samples"
    ),
    "mse": (
        "MSE (Mean Squared Error) is the average squared difference "
        "between actual and predicted values.\n"
        "Formula: sum((actual - predicted)^2) / number of samples"
    ),
    "r2": (
        "R-squared measures how well a regression model explains variation "
        "relative to predicting the target mean. It can be negative, and "
        "a value closer to 1 is generally better."
    ),
    "standardization": (
        "Standardization scales a feature using its mean and standard "
        "deviation.\nFormula: z = (x - mean) / standard deviation. "
        "The transformed feature has mean 0 and standard deviation 1 "
        "when calculated on the data used to fit the scaler."
    ),
    "normalization": (
        "Min-Max normalization commonly rescales values to the range 0 to 1.\n"
        "Formula: (x - minimum) / (maximum - minimum)."
    ),
    "transformer": (
        "A Transformer is a neural network architecture that uses self-attention "
        "to learn relationships between tokens. It is used in many modern "
        "language models, including GPT-style models and BERT."
    ),
    "bias variance": (
        "Bias is error caused by overly simplistic model assumptions; high "
        "bias often causes underfitting. Variance is sensitivity to training "
        "data; high variance often causes overfitting."
    ),
    "type 1 error": (
        "Type 1 error is rejecting a true null hypothesis, also called a "
        "false positive."
    ),
    "type 2 error": (
        "Type 2 error is failing to reject a false null hypothesis, also "
        "called a false negative."
    ),
    "validation": (
        "Validation evaluates a model during development to compare models "
        "and tune hyperparameters. Test data is reserved for final evaluation."
    ),
    "guardrails": (
        "Guardrails are safeguards around an AI system. They can validate "
        "inputs and outputs, enforce topic restrictions, protect sensitive "
        "information, and limit unsafe behavior."
    ),
    "llamaindex": (
        "LlamaIndex is a framework for building LLM applications over data. "
        "It supports data connectors, indexing, retrieval, RAG, and agents."
    ),
    "token": (
        "A token is a unit of text processed by a language model. A token "
        "may be a word, part of a word, punctuation, or another text unit."
    ),
    "chunk": (
        "A chunk is a segment of a document used for processing or retrieval, "
        "often in RAG. Documents are split into chunks before embedding and "
        "retrieval."
    )
}




import re

def get_local_ans(que):
    question = que.lower().strip()

    for key in sorted(local_ans,key=len, reverse=True):
        patt = r"(?<!\w)" + re.escape(key) + r"(?!\w)"

        if re.search(patt,que):
            return local_ans[key]
    return None
    
            