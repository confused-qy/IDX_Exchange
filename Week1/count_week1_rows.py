import csv
from pathlib import Path


def count_rows(path: Path) -> int:
    with path.open('r', encoding='utf-8', errors='ignore', newline='') as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        return sum(1 for _ in reader)


def main() -> None:
    root = Path(__file__).resolve().parents[1].parent
    raw = root / 'raw'

    listed_files = sorted(raw.glob('CRMLSListing*.csv')) + [
        root / 'CRMLSListing202602.csv',
        root / 'CRMLSListing202603.csv',
    ]
    sold_files = sorted(raw.glob('CRMLSSold*.csv')) + [
        root / 'CRMLSSold202602.csv',
        root / 'CRMLSSold202603.csv',
    ]

    listed_files = [p for p in listed_files if p.exists()]
    sold_files = [p for p in sold_files if p.exists()]

    listed_counts = [(p.name, count_rows(p)) for p in listed_files]
    sold_counts = [(p.name, count_rows(p)) for p in sold_files]

    listed_total = sum(c for _, c in listed_counts)
    sold_total = sum(c for _, c in sold_counts)
    listed_final = root  / 'Listed_Final.csv'
    sold_final = root /  'Sold_Final.csv'
    listed_final_rows = count_rows(listed_final) if listed_final.exists() else None
    sold_final_rows = count_rows(sold_final) if sold_final.exists() else None

    print('Listed total rows:', f'{listed_total:,}')
    print('Sold total rows:  ', f'{sold_total:,}')
    if listed_final_rows is not None:
        print('Listed_Final rows:', f'{listed_final_rows:,}')
    if sold_final_rows is not None:
        print('Sold_Final rows:  ', f'{sold_final_rows:,}')
    print('')
    print('Listed monthly row counts:')
    for name, c in listed_counts:
        print(f'{name}  {c}')
    print('')
    print('Sold monthly row counts:')
    for name, c in sold_counts:
        print(f'{name}  {c}')


if __name__ == '__main__':
    main()
