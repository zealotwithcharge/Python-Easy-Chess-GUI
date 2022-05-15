with open('d4Dynamite.pgn','r',encoding='utf-8') as f:
    text = f.read()
    pgns = text.split('\n\n[')
    bans = '<>:"/\|?*' 
    for i,pgn in enumerate(pgns):
        if i != 0:
            name_index = pgn.find('[Black "')
            end_index = pgn[name_index+8:].find(']')
            name = pgn[name_index+8:name_index+8+end_index-1]
            print(name)
            for ban in bans:
                name = name.replace(ban,'')
            with open('white_'+name+'.pgn','w',encoding='utf-8') as temp:
                temp.write('['+pgn)
                temp.close()
    f.close()
