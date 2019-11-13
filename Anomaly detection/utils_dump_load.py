#import pickle
import dill as pickle

def dump_to_pickle(content, filename):
    """ Dumps a content to pickle file: filename.

    Parameters:
        content: string
        filename: string
    """
    pickle_out = open(filename, "wb")
    pickle.dump(content, pickle_out)
    pickle_out.close()


def load_from_pickle(filename):
    """ Loads the content of a pickle file.

    Parameters:
        filename: string
    Returns:
        content: string
    """
    pickle_in = open(filename, "rb")
    return pickle.load(pickle_in)


def dump_to_txt(content, filename, mode="w"):
    """ Dumps a content to txt file: filename.

    Parameters:
        content: string
        filename: string
    """
    File_object = open(filename, mode)
    File_object.write(content)
    File_object.close()


def load_from_txt(filename):
    """ Loads the content of a txt file.

    Parameters:
        filename: string
    Returns:
        content: string
    """
    File_object = open(filename,"r")
    return File_object.read()
