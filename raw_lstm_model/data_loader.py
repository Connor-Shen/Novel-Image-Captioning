import os

import nltk
import torch.utils.data as data

from dataset import CoCoDataset

nltk.download("punkt")


def get_loader(
    transform,
    mode="train",
    type = "None",
    batch_size=1,
    vocab_threshold=None,
    vocab_file="./vocab.pkl",
    start_word="<start>",
    end_word="<end>",
    unk_word="<unk>",
    vocab_from_file=True,
    num_workers=0,
    cocoapi_loc="/opt",
):
    """Returns the data loader.
    Args:
      transform: Image transform.
      mode: One of 'train' or 'test'.
      batch_size: Batch size (if in testing mode, must have batch_size=1).
      vocab_threshold: Minimum word count threshold.
      vocab_file: File containing the vocabulary.
      start_word: Special word denoting sentence start.
      end_word: Special word denoting sentence end.
      unk_word: Special word denoting unknown words.
      vocab_from_file: If False, create vocab from scratch and override any existing vocab_file.
                       If True, load vocab from existing vocab_file, if it exists.
      num_workers: Number of subprocesses to use for data loading.
      cocoapi_loc: The location of the folder containing the COCO API: https://github.com/cocodataset/cocoapi
    """

    assert mode in ["train", "test"], "mode must be one of 'train' or 'test'."

    if not vocab_from_file:
        assert (
            mode == "train"
        ), "To generate vocab from captions file, must be in training mode (mode='train')."

    # Based on mode (train, val, test), obtain img_folder and annotations_file.
    if mode == "train":
        if vocab_from_file:
            assert os.path.exists(
                vocab_file
            ), "vocab_file does not exist. Change vocab_from_file to False to create vocab_file."
        img_folder = os.path.join(cocoapi_loc, "train2014/")
        annotations_file = os.path.join(
            cocoapi_loc, "annotations_DCC/captions_no_caption_rm_eightCluster_train2014.json"
        )

    elif mode == "test" and type == "bottle":
        assert batch_size == 1, "Please change batch_size to 1 if testing the model."
        assert os.path.exists(
            vocab_file
        ), "Must first generate vocab.pkl from training data."
        assert vocab_from_file, "Change vocab_from_file to True."
        img_folder = os.path.join(cocoapi_loc, "val2014/")
        annotations_file = os.path.join(
            cocoapi_loc, "annotations_DCC/captions_split_set_bottle_val_test_novel2014.json"
        )

    # eight cluster
    elif mode == "test" and type == "bottle":
        assert batch_size == 1, "Please change batch_size to 1 if testing the model."
        assert os.path.exists(
            vocab_file
        ), "Must first generate vocab.pkl from training data."
        assert vocab_from_file, "Change vocab_from_file to True."
        img_folder = os.path.join(cocoapi_loc, "val2014/")
        annotations_file = os.path.join(
            cocoapi_loc, "annotations_DCC/captions_split_set_bottle_val_test_novel2014.json"
        )
    elif mode == "test" and type == "bus":
        assert batch_size == 1, "Please change batch_size to 1 if testing the model."
        assert os.path.exists(
            vocab_file
        ), "Must first generate vocab.pkl from training data."
        assert vocab_from_file, "Change vocab_from_file to True."
        img_folder = os.path.join(cocoapi_loc, "val2014/")
        annotations_file = os.path.join(
            cocoapi_loc, "annotations_DCC/captions_split_set_bus_val_test_novel2014.json"
        )
    elif mode == "test" and type == "couch":
        assert batch_size == 1, "Please change batch_size to 1 if testing the model."
        assert os.path.exists(
            vocab_file
        ), "Must first generate vocab.pkl from training data."
        assert vocab_from_file, "Change vocab_from_file to True."
        img_folder = os.path.join(cocoapi_loc, "val2014/")
        annotations_file = os.path.join(
            cocoapi_loc, "annotations_DCC/captions_split_set_couch_val_test_novel2014"
        )
    elif mode == "test" and type == "microwave":
        assert batch_size == 1, "Please change batch_size to 1 if testing the model."
        assert os.path.exists(
            vocab_file
        ), "Must first generate vocab.pkl from training data."
        assert vocab_from_file, "Change vocab_from_file to True."
        img_folder = os.path.join(cocoapi_loc, "val2014/")
        annotations_file = os.path.join(
            cocoapi_loc, "annotations_DCC/captions_split_set_microwave_val_test_novel2014.json"
        )
    elif mode == "test" and type == "pizza":
        assert batch_size == 1, "Please change batch_size to 1 if testing the model."
        assert os.path.exists(
            vocab_file
        ), "Must first generate vocab.pkl from training data."
        assert vocab_from_file, "Change vocab_from_file to True."
        img_folder = os.path.join(cocoapi_loc, "val2014/")
        annotations_file = os.path.join(
            cocoapi_loc, "annotations_DCC/captions_split_set_pizza_val_test_novel2014.json"
        )
    elif mode == "test" and type == "racket":
        assert batch_size == 1, "Please change batch_size to 1 if testing the model."
        assert os.path.exists(
            vocab_file
        ), "Must first generate vocab.pkl from training data."
        assert vocab_from_file, "Change vocab_from_file to True."
        img_folder = os.path.join(cocoapi_loc, "val2014/")
        annotations_file = os.path.join(
            cocoapi_loc, "annotations_DCC/captions_split_set_racket_val_test_novel2014.json"
        )
    elif mode == "test" and type == "suitcase":
        assert batch_size == 1, "Please change batch_size to 1 if testing the model."
        assert os.path.exists(
            vocab_file
        ), "Must first generate vocab.pkl from training data."
        assert vocab_from_file, "Change vocab_from_file to True."
        img_folder = os.path.join(cocoapi_loc, "val2014/")
        annotations_file = os.path.join(
            cocoapi_loc, "annotations_DCC/captions_split_set_suitcase_val_test_novel2014.json"
        )
    elif mode == "test" and type == "zebra":
        assert batch_size == 1, "Please change batch_size to 1 if testing the model."
        assert os.path.exists(
            vocab_file
        ), "Must first generate vocab.pkl from training data."
        assert vocab_from_file, "Change vocab_from_file to True."
        img_folder = os.path.join(cocoapi_loc, "val2014/")
        annotations_file = os.path.join(
            cocoapi_loc, "annotations_DCC/captions_split_set_zebra_val_test_novel2014.json"
        )
    
    else:
        raise ValueError(f"Invalid mode: {mode}")

    # COCO caption dataset.
    dataset = CoCoDataset(
        transform=transform,
        mode=mode,
        batch_size=batch_size,
        vocab_threshold=vocab_threshold,
        vocab_file=vocab_file,
        start_word=start_word,
        end_word=end_word,
        unk_word=unk_word,
        annotations_file=annotations_file,
        vocab_from_file=vocab_from_file,
        img_folder=img_folder,
    )

    if mode == "train":
        print("*********")
        print(annotations_file)
        # Randomly sample a caption length, and sample indices with that length.
        indices = dataset.get_train_indices()
        # Create and assign a batch sampler to retrieve a batch with the sampled indices.
        initial_sampler = data.sampler.SubsetRandomSampler(indices=indices)
        # data loader for COCO dataset.
        data_loader = data.DataLoader(
            dataset=dataset,
            num_workers=num_workers,
            batch_sampler=data.sampler.BatchSampler(
                sampler=initial_sampler, batch_size=dataset.batch_size, drop_last=False
            ),
        )
    else:
        data_loader = data.DataLoader(
            dataset=dataset,
            batch_size=dataset.batch_size,
            shuffle=True,
            num_workers=num_workers,
        )

    return data_loader