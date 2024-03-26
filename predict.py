import argparse

def predict(image_path, checkpoint, top_k, category_names, gpu):
    # Your prediction code here
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict flower name from an image')

    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('checkpoint', type=str, help='Path to the checkpoint file')
    parser.add_argument('--top_k', type=int, default=1, help='Return top K most likely classes')
    parser.add_argument('--category_names', type=str, default='cat_to_name.json', help='Path to category names mapping file')
    parser.add_argument('--gpu', action='store_true', help='Use GPU for inference')

    args = parser.parse_args()

    predict(args.image_path, args.checkpoint, args.top_k, args.category_names, args.gpu)