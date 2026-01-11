const questions = [
  "What is a null graph?",
  "What defines a directed graph?",
  "What is a non-directed graph?",
  "What is a self loop in a graph?",
  "What is a proper edge?",
  "What are multiedges?",
  "What is a simple graph?",
  "What is a multigraph?",
  "What is a pseudo graph?",
  "What is incidence in graph theory?",
  "What does adjacency mean in graphs?",
  "What is the degree of a vertex?",
  "What is an isolated vertex?",
  "What is a pendant vertex?",
  "What is a finite graph?",
  "What is an infinite graph?",
  "What is a complete graph?",
  "What is a regular graph?",
  "What is a bipartite graph?",
  "What is a connected graph?",
  "What is a complete bipartite graph?",
  "What is a subgraph?",
  "What is decomposition of a graph?",
  "What is the complement of a graph?",
  "What is a planar graph?",
  "What does the handshaking theorem state?",
  "What is a walk in graph theory?",
  "What is the length of a walk?",
  "What is a closed walk?",
  "What is an open walk?",
  "What is a trail?",
  "What is a circuit?",
  "What is a path?",
  "What is a cycle?",
  "What is an Eulerian path?",
  "What is an Eulerian circuit?",
  "What is an Eulerian graph?",
  "What is a Hamiltonian path?",
  "What is a Hamiltonian circuit?",
  "What is a Hamiltonian graph?",
  "What is a tree?",
  "What is a rooted tree?",
  "What is a binary tree?",
  "What is a pendant vertex in a tree?",
  "What is path length of a tree?",
  "What is a spanning tree?"
];

const answers = [
  "A graph consisting of n vertices and no edges",
  "A graph that has direction in edges",
  "Edges have no direction",
  "An edge that has same vertex for both its ends",
  "An edge which is not a self loop",
  "Two or more edges have same vertex",
  "A graph that doesn't contain any self loop",
  "Contains multiedge but no self loop",
  "Contains multiedges and a self loop",
  "If e connects v1 and v2 then e is incident",
  "If v1 and v2 are connected by e then v1 and v2 are adjacent",
  "Number of edges that are connected to a vertex",
  "A vertex whose degree is 0",
  "A vertex whose degree is 1",
  "A graph with finite number of vertices and edges",
  "A graph with infinite number of vertices or edges or both",
  "A graph where each vertex is connected to every other vertex",
  "A graph where each vertex has same degree",
  "A graph whose vertices can be partitioned into two disjoint sets X and Y",
  "A graph where each vertex is connected to at least 2 vertices",
  "A bipartite graph where every vertex in X is connected to every vertex in Y",
  "A small portion of a big graph",
  "A graph decomposed into two subgraphs G1 and G2 if G1∪G2=G and G1∩G2=null",
  "A simple graph with same vertex set where two vertices are adjacent only when not adjacent in G",
  "A graph which can be drawn in a plane so its edges don't cross",
  "The sum of degree of vertices equals twice the number of edges",
  "A finite alternating sequence of vertices and edges",
  "The number of edges in a walk",
  "A walk where starting and ending vertices are the same",
  "A walk where starting and ending vertices are different",
  "A walk having different edges",
  "A closed trail",
  "A walk with different vertices",
  "A closed path",
  "A path that covers all edges without repetition",
  "A circuit that covers all edges without repeating",
  "A connected graph which contains an Eulerian circuit",
  "A path that covers every vertex without repetition",
  "A circuit that passes through each vertex exactly once except starting and ending vertex",
  "A connected graph that contains a Hamiltonian circuit",
  "A connected graph without any cycles",
  "A tree where one vertex is designated as root",
  "A tree that has exactly one vertex of degree 2",
  "A vertex in a tree with degree 1",
  "The sum of edges from the root to all pendant vertices",
  "A subgraph of G which is a tree and includes all vertices of G"
];

let answer = "";

function shuffle(array) {
    for (let x = (array.length + 1) - 1; x > 0; x--) {
        let y = Math.floor(Math.random() * (x + 1));
        [array[x], array[y]] = [array[y], array[x]];
    }
    return array;
}

function loadquestions(Qs, ans) {
    let j = Math.floor(Math.random() * Qs.length);
    let question = Qs[j];
    answer = ans[j];
    let options = ans.filter(a => a !== answer);
    options = shuffle(options).slice(0, 3);
    let newoptions = options.slice(0, 3);
    let randomIndex = Math.floor(Math.random() * 4);
    newoptions.splice(randomIndex, 0, answer);
    document.getElementById("question").innerText = `Q. ${question}`;
    document.getElementById("o1").innerText = `${newoptions[0]}`;
    document.getElementById("o2").innerText = `${newoptions[1]}`;
    document.getElementById("o3").innerText = `${newoptions[2]}`;
    document.getElementById("o4").innerText = `${newoptions[3]}`;
}

loadquestions(questions, answers);

function checkAnswer(elm) {
    selectedtxt = elm.innerText;
    if (selectedtxt === answer) {
        loadquestions(questions, answers);
    } else {
        loadquestions(questions, answers);
    }
}
