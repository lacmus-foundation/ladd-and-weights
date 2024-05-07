import argparse
import os
import hashlib
import pathlib
import shutil
from tqdm import tqdm
import random


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Merge LADD',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-d', '--dir',
        required=True,
        type=str,
        help='Directory containing LADD files',
        default='dataset'
    )
    return parser.parse_args()


def find_datasets(dir: str) -> list[str]:
    print(dir)
    datasets = []

    if 'Annotations' in os.listdir(dir):
        return [dir]

    for d in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, d)):
            datasets += find_datasets(os.path.join(dir, d))

    return datasets


def merge_datasets(dirs: list[str], outdir: str) -> None:
    out_annotations = os.path.join(outdir, 'Annotations')
    out_images = os.path.join(outdir, 'ImageSets', 'Main')
    out_jpeg_images = os.path.join(outdir, 'JPEGImages')
    names = []
    os.makedirs(outdir, exist_ok=True)
    os.makedirs(out_annotations, exist_ok=True)
    os.makedirs(out_images, exist_ok=True)
    os.makedirs(out_jpeg_images, exist_ok=True)

    for dataset in dirs:
        print(f'Merging {dataset}')
        annotations = os.listdir(os.path.join(dataset, 'Annotations'))
        for annotation in tqdm(annotations):
            old_name = pathlib.Path(annotation).stem
            old_annotation = os.path.join(dataset, 'Annotations', annotation)
            old_image = os.path.join(dataset, 'JPEGImages', old_name + '.jpg')
            if not os.path.exists(old_annotation):
                print(f'Skipped {old_name}')
                continue
            if not os.path.exists(old_image):
                print(f'Skipped {old_name}')
                continue

            new_name = hashlib.md5(open(old_image, 'rb').read()).hexdigest()
            names.append(new_name)

            new_annotation = os.path.join(out_annotations, f'{new_name}.xml')
            new_image = os.path.join(out_images, f'{new_name}.jpg')

            shutil.copy(old_image, new_image)
            annotation_text = open(old_annotation, 'r').read()
            annotation_text = annotation_text.replace(
                f'<filename>{old_name}</filename>',
                f'<filename>{new_name}</filename>'
            )
            annotation_text = annotation_text.replace(
                f'<filename>{old_name.replace('train_', '')}</filename>',
                f'<filename>{new_name}</filename>'
            )
            annotation_text = annotation_text.replace(
                f'<filename>{old_name.replace('test_', '')}</filename>',
                f'<filename>{new_name}</filename>'
            )
            open(new_annotation, 'w').write(annotation_text)

    random.shuffle(names)

    train_names = names[:int(len(names) * 0.75)]
    test_names = names[int(len(names) * 0.75):]

    open(os.path.join(out_images, 'train.txt'), 'w').write('\n'.join(train_names))
    open(os.path.join(out_images, 'trainval.txt'), 'w').write('\n'.join(train_names))
    open(os.path.join(out_images, 'val.txt'), 'w').write('\n'.join(test_names))
    open(os.path.join(out_images, 'test.txt'), 'w').write('\n'.join(test_names))


def main():
    args = parse_args()
    datasets = find_datasets(args.dir)

    print(f'Merging {len(datasets)} datasets:')
    for dataset in datasets:
        print(f'\t{dataset}')

    merge_datasets(datasets, os.path.join(args.dir, 'full_train_ds'))


if __name__ == '__main__':
    main()


