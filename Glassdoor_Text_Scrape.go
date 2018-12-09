package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/PuerkitoBio/goquery"
)

func init() {
	log.SetFlags(log.Lshortfile)
}

func main() {
	page := 1
	for {
		u := fmt.Sprintf("https://www.glassdoor.com/Reviews/ADP-Reviews-E64_P%d.htm", page)
		req, err := http.NewRequest("GET", u, nil)
		if err != nil {
			log.Fatal(err)
		}
		req.Header.Set("Authority", "www.glassdoor.com")
		req.Header.Set("Upgrade-Insecure-Requests", "1")
		req.Header.Set("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
		req.Header.Set("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
		req.Header.Set("Referer", "https://www.glassdoor.com/")
		req.Header.Set("Accept-Language", "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7")
		req.Header.Set("Cookie", "JSESSIONID=4E48E09C9DA541028771235B693ED4E7; GSESSIONID=4E48E09C9DA541028771235B693ED4E7; gdId=bf142246-252c-4026-8c1c-6843899f64a3; trs=direct:direct:direct:2018-10-23+18%3A01%3A23.88:undefined:undefined; _ga=GA1.2.1802192054.1540342887; _gid=GA1.2.422185282.1540342887; JSESSIONID_JX_APP=19B478F54B9FB80A19867F1531D3B7D7; _gcl_au=1.1.2130559101.1540342887; __gads=ID=80f8fa1c2d274f6d:T=1540342887:S=ALNI_Maa5GHVhFd0MnPnyUsxBP0wqMxBcQ; ht=%7B%22quantcast%22%3A%5B%22D%22%5D%7D; __qca=P0-1085123878-1540342888510; G_ENABLED_IDPS=google; rm=YmFvem91bWFuaHVhQGdteC5jb206MTU3MTkwMDUzOTY3NzpmYzAzOTE3YTA3M2ZlZGM2NTg2ODFkYzU2MDIzYjY5Mg; _uac=00000166a398001e903cb5e16749b7da; JSESSIONID_KYWI_APP=04A811C880328473302F35223B452CB6; newUserOnboarding=false; _mibhv=anon-1540342942309-3008285835_6890; ki_t=1540342945282%3B1540342945282%3B1540342945282%3B1%3B1; ki_r=; __gdpopuc=1; uc=8F0D0CFA50133D96DAB3D34ABA1B87337CCBB5D7EC19A1D64236C43B3B8EED4A1033DBFC537B581B694B79677CC20705428FFA29865D51AEA85EE889C7A322F6288DF43307307CC07DAA406CBA410D5FE57273BD4C66BE6560A417FFE204A5C9095531C31D505188954D6D49C0D2787B24D0795DA3E8172BEF43C247B2F8BD56F72394AE22DDBBC97439F6DFB5C1EC2BF3A56E76A5D3A05B; cass=1; cto_lwid=04a25574-d20d-4795-a980-d352610b086b; AWSALB=Abo6Ewo+0C1UJL3+2L2bjjzviEw2Q7yfMF4O3J+Uk66TQOv5Dw891UXmRQUzhiEYDze+qbkta//JmJ7PZcbHhUx8jNhkLzFLp6Z3Lomt9yxtdtPoEehxh0b45pXDnt+LY2TOMypabNxxUGNZF5ib+1v3J4uNPfygY9Jrs2t98/YvGMt/sNBKBNB4toeL2IwBDaU5rN9c6O4/Yj/B5Gs7F2XDFTSlCbDoKsnOWRqW2I31cZ3shC1MZxiXK77ItBA=")

		resp, err := http.DefaultClient.Do(req)
		if err != nil {
			log.Fatal(err)
		}
		defer resp.Body.Close()

		writer := csv.NewWriter(os.Stdout)
		document, err := goquery.NewDocumentFromReader(resp.Body)
		if err != nil {
			log.Fatal(err)
		}
		document.Find("li.empReview").Each(func(i int, review *goquery.Selection) {
			var entry []string

			// id
			id, ok := review.Attr("id")
			if !ok {
				return
			}
			entry = append(entry, id)

			// date
			datetime, ok := review.Find("time").Attr("datetime")
			if ok {
				entry = append(entry, datetime)
			} else {
				entry = append(entry, "")
			}

			// star
			star, ok := review.Find(".gdStarsWrapper .value-title").Attr("title")
			if ok {
				entry = append(entry, star)
			} else {
				entry = append(entry, "")
			}

			// position
			entry = append(entry, review.Find("span.authorJobTitle.middle.reviewer").Text())

			// status
			entry = append(entry, review.Find("p.tightBot.mainText").Text())

			// summary
			entry = append(entry, review.Find("span.summary").Text())

			// pros
			entry = append(entry, review.Find("p.pros.mainText").Text())

			// cons
			entry = append(entry, review.Find("p.cons.mainText").Text())

			writer.Write(entry)
			writer.Flush()
		})
		if document.Find("li.next>span.disabled").Length() != 0 {
			return
		} else {
			fmt.Fprintln(os.Stderr, page)
			page++
		}
		time.Sleep(time.Second)
	}
}
