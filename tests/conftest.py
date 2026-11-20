import pytest


@pytest.fixture
def sample_csv(tmp_path):
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(
        "price,quantity\n10000,2\n5000,3\n",
        encoding="utf-8",
    )
    return csv_file
