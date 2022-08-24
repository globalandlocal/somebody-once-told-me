with open('input.txt', 'r', encoding='utf-8') as inp , open('output.txt' , 'w' , encoding='utf-8') as out :
    all_graph = set()
    graph_mass = {}
    for _ in range(int(inp.readline())):
        inp_line=inp.readline().strip()
        for i in range(len(inp_line)-3):
            c=(inp_line[i:i+3],inp_line[i+1:i+4])
            if c in graph_mass :
                graph_mass[c] += 1
            else:
                graph_mass[c] = 1
            if c[0] not in all_graph :
                all_graph.add(c[0])
        all_graph.add(c[1])
    print(len(all_graph) , file=out)
    print(len(graph_mass) , file=out)
    for k in graph_mass:
        print( *k , graph_mass[k] , file=out)
