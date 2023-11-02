import os
import toolkit_config as cfg
import yf_example2
import yfinance as yf


def qan_prc_to_csv(year):
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"

    tic = "QAN.AX"
    data = yf.download(tic, start=start_date, end=end_date, ignore_tz=True)
    filename = f"qan_prc_{year}.csv"
    file_path = os.path.join(cfg.DATADIR, filename)

    data.to_csv(file_path)


if __name__ == "__main__":
    qan_prc_to_csv(2020)
