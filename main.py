import json
import os
from icrawler.builtin import GoogleImageCrawler, BingImageCrawler, BaiduImageCrawler, FlickrImageCrawler, GreedyImageCrawler
from rename import rename_files


def main():
    # 検索したい名前
    print("検索したいキーワードを入力してください")
    searchName = input()

    # config.jsonから保存先のパスを取得
    confiug_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(confiug_path, "r", encoding='utf-8') as f:
        config = json.load(f)

    # 保存先のパスに検索したい名前を追加しディレクトリを作成
    savePath = config["DIR_PATH"] + searchName

    # どのサイトから画像を取得するかを指定
    print("\n\n検索したいサイトの数字を選択してください")
    print("デフォルトを選択する場合はそのままEnterを押してください")
    print("1:Google  --default")
    print("2:Bing")
    print("3:Baidu")
    print("4:Flick")
    print("5:Greedy")

    # 無限ループ
    site = ""
    while site not in ["1", "2", "3", "4", "5"]:
        site = input()
        if site == "1" or site == "":
            # どのサイトから画像を取得するかを指定
            crawler = GoogleImageCrawler(storage={"root_dir": savePath})
            print("Googleから画像を取得します")
            prefix = "fromGoogle"
            # デフォルトの場合は1を代入
            site = "1"
        elif site == "2":
            crawler = BingImageCrawler(storage={"root_dir": savePath})
            print("Bingから画像を取得します")
            prefix = "fromBing"
        elif site == "3":
            crawler = BaiduImageCrawler(storage={"root_dir": savePath})
            print("Baiduから画像を取得します")
            prefix = "fromBaidu"
        elif site == "4":
            crawler = FlickrImageCrawler(storage={"root_dir": savePath})
            print("Flickrから画像を取得します")
            prefix = "fromFlickr"
        elif site == "5":
            crawler = GreedyImageCrawler(storage={"root_dir": savePath})
            print("Greedyから画像を取得します")
            prefix = "fromGreedy"
        else:
            print("半角1~5の数字を入力してください")

    # 何件の画像をダウンロードするかを指定
    print("\n\n何件の画像をダウンロードしますか？ デフォルトは100件です")
    print("必ずしも指定した件数の画像がダウンロードされるわけではありません")
    tmp = input()
    if tmp == "":
        max_num = 100
    else:
        max_num = tmp

    # 変更する名前を指定
    print("\n\n先頭に付ける名前を入力してください")
    print("何も入力しない場合は選択したサイトの名前が付けられます")
    tmp = input()
    if tmp == "":
        pass
    else:
        prefix = tmp

    # 画像をダウンロード
    print("画像をダウンロードします")
    crawler.crawl(keyword=searchName, max_num=max_num)

    # 連番のファイル名を指定した名前に変更
    rename_files(savePath, prefix)


if __name__ == '__main__':
    main()
