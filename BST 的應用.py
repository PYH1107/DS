# 1. 創建節點類別（Node）：
    #首先，你可以定義一個節點類別，其中包含歌曲的相關資訊，如標題、藝術家、時長等。
    #這個節點類別可以包含左子樹和右子樹的參考。
class Node:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.left = None
        self.right = None

#2. 創建播放列表類別（Playlist）
    #接下來，你可以定義一個播放列表類別，該類別內部包含一個BST的根節點。
    # 該類別提供了添加歌曲、按標題搜尋歌曲以及播放歌曲等功能。
class Playlist:
    def __init__(self):
        self.root = None

    def add_song(self, title, artist, duration):
        # 創建新節點
        new_song = Node(title, artist, duration)

        if self.root is None:
            # 如果根節點為空，將新節點設置為根節點
            self.root = new_song
        else:
            # 否則，尋找適當的位置插入新節點
            current = self.root
            while True:
                if title < current.title:
                    # 插入到左子樹
                    if current.left is None:
                        current.left = new_song
                        break
                    else:
                        current = current.left
                else:
                    # 插入到右子樹
                    if current.right is None:
                        current.right = new_song
                        break
                    else:
                        current = current.right

    def search_song(self, title):
        # 在BST上搜索特定標題的歌曲
        current = self.root
        while current is not None:
            if title == current.title:
                # 找到歌曲
                return current
            elif title < current.title:
                # 在左子樹中繼續搜索
                current = current.left
            else:
                # 在右子樹中繼續搜索
                current = current.right

        # 如果沒有找到歌曲，返回None
        return None

    def play_song(self, title):
        song = self.search_song(title)
        if song is not None:
            # 播放歌曲
            print("Playing:", song.title, "-", song.artist)
        else:
            print("Song not found.")

#3. 測試播放列表：現在，你可以創建一個播放列表並測試它的功能。
# 創建播放列表
playlist = Playlist()

# 添加歌曲
playlist.add_song("Song A", "Artist A", 180)
playlist.add_song("Song B", "Artist B", 240)
playlist.add_song("Song C", "Artist C", 200)
playlist.add_song("Song D", "Artist D", 150)

# 播放歌曲
playlist.play_song("Song B")  # Playing: Song B - Artist B
playlist.play_song("Song D")  # Playing: Song D - Artist D
playlist.play_song("Song E")  # Song not found.

# Memo to myself (230604，14:09。理圖):
    # 比起BST，ChatGPT所給的這個範例更像是單純的binary search 而已。
    # 因為並未使用到 "a valid binary search tree" 的定義 (也無法比大小)
    # 但如果能加以修改(ex. 多聽一次這首歌就為它加一分，最後構建成BST。實現有效的管理跟喜好查詢/分類)
    #Conclusion: 不清楚現在串流平台的推薦/算法機制如何運行，但從這個發想中總覺得離那些厲害的酷東西更進一步了!)