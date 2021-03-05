from scrapy import cmdline

if __name__ == '__main__':
	# cmdline.execute("scrapy crawl t1".split())
	cmdline.execute("scrapy crawl t1 -a begin_num=10".split())
