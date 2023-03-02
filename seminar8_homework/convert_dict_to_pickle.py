import pickle


def convert_to_pickle(data: dict) -> None:
    with open('result.pickle', 'wb') as f:
        pickle.dump(data, f)