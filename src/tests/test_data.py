from src.data import read_raw_data, preprocess_data, get_featues, get_label


def test_raw_shape():
    dframe = read_raw_data()
    assert dframe.shape == (150, 5)


def test_get_features_shape():
    dframe = read_raw_data()
    processed = preprocess_data(dframe)
    features = get_featues(processed)
    label = get_label(processed)

    assert features.shape == (150, 4)
    assert label.shape == (150,)
