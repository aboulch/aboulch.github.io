import csv

def write_pub(file, pub, dict_keys):
    
    
    file.write('<div class="archive__row">')
    file.write('<img align="left" style="padding-right: 10px; padding-top: 5px; padding-bottom: 5px" src="/images/publications/{}"> \n\n'.format(pub[dict_keys['teaser']])) if pub[dict_keys['teaser']] is not "" else None

    file.write('<div class="archive__column_text">')
    file.write("<small>\n")
    file.write(f"<b>{pub[dict_keys['title']]}</b><br/>")
    file.write(f"in {pub[dict_keys['venue']]}, {pub[dict_keys['date']]}<br/>")
    file.write(f"also in {pub[dict_keys['additional_venue']]}<br/>")if pub[dict_keys['additional_venue']] is not "" else None
    file.write(f"{pub[dict_keys['note']]}<br/>")if pub[dict_keys['note']] is not "" else None
    file.write(f"<i>{pub[dict_keys['authors']]}</i><br/>")

    file.write('<a href="{}">Paper</a>&nbsp;&nbsp;'.format(pub[dict_keys['url']])) if pub[dict_keys['url']] is not "" else None
    file.write('<a href="{}">Arxiv</a>&nbsp;&nbsp;'.format(pub[dict_keys['arxiv']])) if pub[dict_keys['arxiv']] is not "" else None
    file.write('<a href="{}">HAL</a>&nbsp;&nbsp;'.format(pub[dict_keys['hal']])) if pub[dict_keys['hal']] is not "" else None
    file.write('<a href="{}">PDF</a>&nbsp;&nbsp;'.format(pub[dict_keys['pdf']])) if pub[dict_keys['pdf']] is not "" else None
    file.write('<a href="{}">Slides</a>&nbsp;&nbsp;'.format(pub[dict_keys['slides']])) if pub[dict_keys['slides']] is not "" else None
    file.write('<a href="{}">Poster</a>&nbsp;&nbsp;'.format(pub[dict_keys['poster']])) if pub[dict_keys['poster']] is not "" else None
    file.write('<a href="{}">Code</a>&nbsp;&nbsp;'.format(pub[dict_keys['code']])) if pub[dict_keys['code']] is not "" else None

    file.write("</small>")
    file.write("</div>")
    file.write("</div>")
    file.write("\n\n")


with open('publications.csv', 'r') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # get the keys
    for row in filereader:
        # print(', '.join(row))
        keys = row
        break
    print("Keys", keys)
    
    dict_keys = {}
    for key_id, key in enumerate(keys):
        dict_keys[key] = key_id

    # getting the publications
    publications = []
    for row in filereader:
        publications.append(row)

    # creating the markdown file (date sorting)
    dates = []
    for pub in publications:
        dates.append(pub[dict_keys["date"]])
    date_indices = [i[0] for i in sorted(enumerate(dates), key=lambda x:x[1])]
    dates_sorted_publications = []
    for index in date_indices:
        dates_sorted_publications.append(publications[index])
    dates_sorted_publications = dates_sorted_publications[::-1]
    
    with open("../_pages/publications_year.md", "w") as file:

        # write the header
        file.write('---\n')
        file.write('layout: archive_pub\n')
        file.write('title: "Publications"\n')
        file.write('permalink: /publications_year/\n')
        file.write('author_profile: true\n')
        file.write('redirect_from:\n')
        file.write('- /resume\n')
        file.write('---\n')
        file.write('{% include base_path %}\n')

        file.write("### [Sort publications by type](/publications_type)\n\n")

        prev_year = ""
        for pub in dates_sorted_publications:
            if pub[dict_keys["date"]] != prev_year:
                file.write("### {}\n\n".format(pub[dict_keys["date"]]))
                prev_year = pub[dict_keys["date"]]
            write_pub(file, pub, dict_keys)

    used = [False for _ in publications]
    order = [["journal","Journal"], ["conference","Conference"], ["arxiv","Arxiv"], ["misc", "Misc"]]
    with open("../_pages/publications_type.md", "w") as file:

        # write the header
        file.write('---\n')
        file.write('layout: archive_pub\n')
        file.write('title: "Publications"\n')
        file.write('permalink: /publications_type/\n')
        file.write('author_profile: true\n')
        file.write('redirect_from:\n')
        file.write('- /resume\n')
        file.write('---\n')
        file.write('{% include base_path %}\n')

        file.write("### [Sort publications by date](/publications_year)\n\n")

        for item in order:

            pub_tmp = []
            for pub_id, pub in enumerate(dates_sorted_publications):
                if pub[dict_keys['type']] == item[0]:
                    used[pub_id] = True
                    pub_tmp.append(pub)
                if item == "misc" and not used[pub_id]:
                    pub_tmp.append(pub)

            if len(pub_tmp) > 0:
                file.write(f"## {item[1]}\n")
                for pub in dates_sorted_publications:
                    if pub[dict_keys['type']] == item[0]:
                        write_pub(file, pub, dict_keys)
