import traceback
import time
import datetime
import math

import db
import download
import help_text
import args

exclude = args.get_list('exclude')
download_companies = 'companies' not in exclude
download_price_volume = 'priceVolume' not in exclude

connection_options = {
    'host': args.get('host'),
    'password': args.get('password'),
    'user': args.get('user'),
    'dbname': args.get('dbname'),
    'port': args.get('port')
}

if args.exists('help'):
    help_text.print_menu()
    exit(0)

if __name__ == '__main__':
    start = time.time()

    try:
        conn = db.connect(**connection_options)
        curs = conn.cursor()

        db.init(curs)
        conn.commit()

        if download_companies:
            download.companies(curs, conn.commit)

        if download_price_volume:
            download.price_volume(curs, conn.commit)

        curs.close()

        end = time.time()
        total = math.floor(end - start)
        total_time = str(datetime.timedelta(seconds=total))
        print('done {0} h:mm:ss'.format(total_time))
    except KeyboardInterrupt:
        pass
    except Exception:
        traceback.print_exc()
    finally:
        if conn is not None:
            conn.close()
