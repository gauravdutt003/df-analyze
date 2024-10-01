from __future__ import annotations

# fmt: off
import sys  # isort: skip
from pathlib import Path  # isort: skip
ROOT = Path(__file__).resolve().parent.parent.parent.parent  # isort: skip
sys.path.append(str(ROOT))  # isort: skip
# fmt: on

EMBED_DATA = ROOT / "data/testing/embedding"

NLP_ROOT = EMBED_DATA / "NLP"
NLP_CLS = NLP_ROOT / "classification"
NLP_REG = NLP_ROOT / "regression"

VISION_ROOT = EMBED_DATA / "vision"
VISION_CLS = VISION_ROOT / "classification"
VISION_REG = VISION_ROOT / "regression"


CLS_DATAFILES = {
    # needs further processing, hard to use as is, i.e. labels must be max-voted
    # "Aegis-AI-Content-Safety-Dataset-1.0": {
    #     "root": NLP_CLS / "Aegis-AI-Content-Safety-Dataset-1.0",
    #     "train": Path(
    #         "Content Moderation Extracted Annotations 02.08.24_train_release_0418_v1.parquet"
    #     ),
    #     "val": None,
    #     "test": Path(
    #         "Content Moderation Extracted Annotations 02.08.24_test_release_0418_v1.parquet"
    #     ),
    #     "all": None,  # if None, use all of train, val, test after concat
    #     "textcol": "text",
    #     "targetcols": ["labels_0", "labels_1", "labels_2", "labels_3", "labels_4"],
    #     "labelnamecols": [],
    #     "dropcols": ["id", "num_annotations", "text_type"],
    # },
    "ag_news": {
        "root": NLP_CLS / "ag_news",
        "train": Path("data/train-00000-of-00001.parquet"),
        "val": None,
        "test": Path("data/test-00000-of-00001.parquet"),
        "all": NLP_CLS / "ag_news/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "app_reviews": {
        "root": NLP_CLS / "app_reviews",
        "train": Path("data/train-00000-of-00001.parquet"),
        "val": None,
        "test": None,
        "all": Path("data/train-00000-of-00001.parquet"),
        "textcol": "review",
        "targetcols": ["star"],
        "labelnamecols": [],
        "dropcols": ["package_name", "date"],
    },
    "climate_sentiment": {
        "root": NLP_CLS / "climate_sentiment",
        "train": Path("data/train-00000-of-00001-04b49ae22f595095.parquet"),
        "test": Path("data/test-00000-of-00001-3f9f7af4f5914b8e.parquet"),
        "all": NLP_CLS / "climate_sentiment/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "Dynasent_Disagreement": {
        "root": NLP_CLS / "Dynasent_Disagreement",
        "train": Path("train.csv"),
        "val": Path("validation.csv"),
        "test": Path("test.csv"),
        "all": NLP_CLS / "Dynasent_Disagreement/all.parquet",
        "textcol": "text",
        "targetcols": ["binary_disagreement", "disagreement_rate"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "emotion": {
        "root": NLP_CLS / "emotion",
        "train": Path("split/train-00000-of-00001.parquet"),
        "val": Path("split/validation-00000-of-00001.parquet"),
        "test": Path("split/test-00000-of-00001.parquet"),
        "all": Path("unsplit/train-00000-of-00001.parquet"),
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "financial-classification": {
        "root": NLP_CLS / "financial-classification",
        "train": Path("data/train-00000-of-00001.parquet"),
        "test": Path("data/test-00000-of-00001.parquet"),
        "all": NLP_CLS / "financial-classification/all.parquet",
        "textcol": "text",
        "targetcols": ["labels"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "go_emotions": {  # multi-label, needs additional processing
        "root": NLP_CLS / "go_emotions",
        # "train": Path("raw/train-00000-of-00001.parquet"),
        "val": Path("simplified/validation-00000-of-00001.parquet"),
        "test": Path("simplified/test-00000-of-00001.parquet"),
        "train": Path("simplified/train-00000-of-00001.parquet"),
        "all": NLP_CLS / "go_emotions/all.parquet",
        "textcol": "text",
        "targetcols": ["labels"],
        "labelnamecols": [],
        "dropcols": ["id"],
    },
    "multiclass-sentiment-analysis-dataset": {
        "root": NLP_CLS / "multiclass-sentiment-analysis-dataset",
        "train": Path("train_df.csv"),
        "val": Path("val_df.csv"),
        "test": Path("test_df.csv"),
        "all": NLP_CLS / "multiclass-sentiment-analysis-dataset/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": ["sentiment"],
        "dropcols": ["id"],
    },
    "poem_sentiment": {
        "root": NLP_CLS / "poem_sentiment",
        "train": Path("data/train-00000-of-00001.parquet"),
        "val": Path("data/validation-00000-of-00001.parquet"),
        "test": Path("data/test-00000-of-00001.parquet"),
        "all": NLP_CLS / "poem_sentiment/all.parquet",
        "textcol": "verse_text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": ["id"],
    },
    "rotten_tomatoes": {
        "root": NLP_CLS / "rotten_tomatoes",
        "train": Path("train.parquet"),
        "val": Path("validation.parquet"),
        "test": Path("test.parquet"),
        "all": NLP_CLS / "rotten_tomatoes/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "toxic-chat_0124": {
        "root": NLP_CLS / "toxic-chat",
        "train": Path("data/0124/toxic-chat_annotation_train.csv"),
        "test": Path("data/0124/toxic-chat_annotation_test.csv"),
        "all": Path("data/0124/toxic-chat_annotation_all.csv"),
        "textcol": "user_input",
        "targetcols": ["toxicity", "jailbreaking"],
        "labelnamecols": [],
        "dropcols": ["conv_id", "model_output", "openai_moderation", "human_annotation"],
    },
    "toxic-chat_1123": {
        "root": NLP_CLS / "toxic-chat",
        "train": Path("data/1123/toxic-chat_annotation_train.csv"),
        "test": Path("data/1123/toxic-chat_annotation_test.csv"),
        "all": Path("data/1123/toxic-chat_annotation_all.csv"),
        "textcol": "user_input",
        "targetcols": ["toxicity", "jailbreaking"],
        "labelnamecols": [],
        "dropcols": ["conv_id", "model_output", "openai_moderation", "human_annotation"],
    },
    "toxicity_classification_jigsaw": {
        "root": NLP_CLS / "toxicity_classification_jigsaw",
        "train": Path("train_dataset.csv"),
        "val": Path("val_dataset.csv"),
        "test": Path("test_dataset.csv"),
        "all": NLP_CLS / "toxicity_classification_jigsaw/all.parquet",
        "textcol": "comment_text",
        "targetcols": [
            "toxic",
            "severe_toxic",
            "obscene",
            "threat",
            "insult",
            "identity_hate",
        ],
        "labelnamecols": [],
        "dropcols": ["id"],
    },
    "tweet_sentiment_multilingual_arabic": {
        "root": NLP_CLS / "tweet_sentiment_multilingual",
        "train": Path("data/arabic/train.jsonl"),
        "val": Path("data/arabic/validation.jsonl"),
        "test": Path("data/arabic/test.jsonl"),
        "all": NLP_CLS / "tweet_sentiment_multilingual/data/arabic/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "tweet_sentiment_multilingual_english": {
        "root": NLP_CLS / "tweet_sentiment_multilingual",
        "train": Path("data/english/train.jsonl"),
        "val": Path("data/english/validation.jsonl"),
        "test": Path("data/english/test.jsonl"),
        "all": NLP_CLS / "tweet_sentiment_multilingual/data/english/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "tweet_sentiment_multilingual_french": {
        "root": NLP_CLS / "tweet_sentiment_multilingual",
        "train": Path("data/french/train.jsonl"),
        "val": Path("data/french/validation.jsonl"),
        "test": Path("data/french/test.jsonl"),
        "all": NLP_CLS / "tweet_sentiment_multilingual/data/french/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "tweet_sentiment_multilingual_german": {
        "root": NLP_CLS / "tweet_sentiment_multilingual",
        "train": Path("data/german/train.jsonl"),
        "val": Path("data/german/validation.jsonl"),
        "test": Path("data/german/test.jsonl"),
        "all": NLP_CLS / "tweet_sentiment_multilingual/data/german/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "tweet_sentiment_multilingual_hindi": {
        "root": NLP_CLS / "tweet_sentiment_multilingual",
        "train": Path("data/hindi/train.jsonl"),
        "val": Path("data/hindi/validation.jsonl"),
        "test": Path("data/hindi/test.jsonl"),
        "all": NLP_CLS / "tweet_sentiment_multilingual/data/hindi/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "tweet_sentiment_multilingual_italian": {
        "root": NLP_CLS / "tweet_sentiment_multilingual",
        "train": Path("data/italian/train.jsonl"),
        "val": Path("data/italian/validation.jsonl"),
        "test": Path("data/italian/test.jsonl"),
        "all": NLP_CLS / "tweet_sentiment_multilingual/data/italian/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "tweet_sentiment_multilingual_portuguese": {
        "root": NLP_CLS / "tweet_sentiment_multilingual",
        "train": Path("data/portuguese/train.jsonl"),
        "val": Path("data/portuguese/validation.jsonl"),
        "test": Path("data/portuguese/test.jsonl"),
        "all": NLP_CLS / "tweet_sentiment_multilingual/data/portuguese/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "tweet_sentiment_multilingual_spanish": {
        "root": NLP_CLS / "tweet_sentiment_multilingual",
        "train": Path("data/spanish/train.jsonl"),
        "val": Path("data/spanish/validation.jsonl"),
        "test": Path("data/spanish/test.jsonl"),
        "all": NLP_CLS / "tweet_sentiment_multilingual/data/spanish/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "tweet_topic_single_2020": {
        "root": NLP_CLS / "tweet_topic_single",
        "labels": Path("dataset/label.single.json"),
        "train": Path("dataset/split_temporal/train_2020.single.json"),
        "val": Path("dataset/split_temporal/validation_2020.single.json"),
        "test": Path("dataset/split_temporal/test_2020.single.json"),
        "all": NLP_CLS / "tweet_topic_single/all_2020.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": ["label_name"],
        "dropcols": ["date", "id"],
    },
    "tweet_topic_single_2021": {
        "root": NLP_CLS / "tweet_topic_single",
        "labels": Path("dataset/label.single.json"),
        "train": Path("dataset/split_temporal/train_2021.single.json"),
        "val": Path("dataset/split_temporal/validation_2021.single.json"),
        "test": Path("dataset/split_temporal/test_2021.single.json"),
        "all": NLP_CLS / "tweet_topic_single/all_2021.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": ["label_name"],
        "dropcols": ["date", "id"],
    },
    "wiki_toxic": {
        "root": NLP_CLS / "wiki_toxic",
        # "train": Path("balanced_train.csv"),
        "train": Path("train.csv"),
        "val": Path("validation.csv"),
        "test": Path("test.csv"),
        "all": NLP_CLS / "wiki_toxic/all.parquet",
        "textcol": "comment_text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": ["id"],
    },
    "yelp_review_full": {
        "root": NLP_CLS / "yelp_review_full",
        "train": Path("yelp_review_full/train-00000-of-00001.parquet"),
        "val": None,
        "test": Path("yelp_review_full/test-00000-of-00001.parquet"),
        "all": NLP_CLS / "yelp_review_full/all.parquet",
        "textcol": "text",
        "targetcols": ["label"],
        "labelnamecols": [],
        "dropcols": [],
    },
}


REG_DATAFILES = {
    "AITA-Reddit-Dataset": {
        "root": NLP_REG / "AITA-Reddit-Dataset",
        "train": Path("cleaned_dataset.csv"),
        "val": None,
        "test": None,
        "all": NLP_REG / "AITA-Reddit-Dataset/all.parquet",
        "textcol": "text",
        "targetcols": ["score", "verdict"],
        "labelnamecols": [],
        "dropcols": ["id", "title", "comment1", "comment2"],
    },
    "amazon-food-reviews-dataset": {
        "root": NLP_REG / "amazon-food-reviews-dataset",
        "train": Path("Reviews.csv"),
        "val": None,
        "test": None,
        "all": NLP_REG / "amazon-food-reviews-dataset/all.parquet",
        "textcol": "Text",
        "targetcols": ["Score", "HelpfulnessNumerator", "HelpfulnessDenominator"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "readability_arxiv": {
        "root": NLP_REG / "readability",
        "train": Path("arxiv-readability.jsonl"),
        "val": None,
        "test": None,
        "all": NLP_REG / "readability/all_arxiv.parquet",
        "textcol": "text",
        "targetcols": ["grade"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "readability_fineweb": {
        "root": NLP_REG / "readability",
        "train": Path("fineweb-edu-readability.jsonl"),
        "val": None,
        "test": None,
        "all": NLP_REG / "readability/all_fineweb.parquet",
        "textcol": "text",
        "targetcols": ["grade"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "readability_tinystories": {
        "root": NLP_REG / "readability",
        "train": Path("tinystories-readability.jsonl"),
        "val": None,
        "test": None,
        "all": NLP_REG / "readability/all_tinystories.parquet",
        "textcol": "text",
        "targetcols": ["grade"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "readability_wikipedia": {
        "root": NLP_REG / "readability",
        "train": Path("wikipedia-en-readability.jsonl"),
        "val": None,
        "test": None,
        "all": NLP_REG / "readability/all_wikipedia.parquet",
        "textcol": "text",
        "targetcols": ["grade"],
        "labelnamecols": [],
        "dropcols": [],
    },
    "stupidfilter": {
        "root": NLP_REG / "stupidfilter",
        "train": Path("train.csv"),
        # "train": Path("stupidfilter.json"),
        "val": None,
        "test": None,
        "all": NLP_REG / "stupidfilter/all.parquet",
        "textcol": "data",
        "targetcols": ["stupidity"],
        "labelnamecols": [],
        "dropcols": [
            "id",
            "spam",
            "nonenglish",
            "graded",
            "moderator",
            "source",
            "nonstupid",
            "mod_history",
            "num_lowers",
            "num_caps",
            "num_punct",
            "num_space",
            "repeat_emphasis",
            "initial_cap",
            "intercap",
            "word_length",
        ],
    },
    "vitamins-supplements-reviews": {
        "root": NLP_REG / "vitamins-supplements-reviews",
        "train": Path("dataset/train.json"),
        "val": Path("dataset/valid.json"),
        "test": Path("dataset/test.json"),
        "all": NLP_REG / "vitamins-supplements-reviews/all.parquet",
        "textcol": "text",
        "targetcols": ["star"],
        "labelnamecols": [],
        "dropcols": ["brand", "product_name"],
    },
}

if __name__ == "__main__":
    for name, info in CLS_DATAFILES.items():
        print(info["all"])
    for name, info in REG_DATAFILES.items():
        print(info["all"])