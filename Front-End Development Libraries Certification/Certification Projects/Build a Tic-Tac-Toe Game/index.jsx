const { useState } = React;

export function Board() {
  const [board, setBoard] = useState(Array(9).fill(""));
  const [isXTurn, setIsXTurn] = useState(true);
  const [gameStatus, setGameStatus] = useState({
    isGameOver: false,
    winner: "",
  });
  function handleClick(event) {
    const position = Number(event.target.id);
    if (board[position] != "" || gameStatus.isGameOver) {
      return;
    }

    const newBoard = [...board];
    newBoard[position] = isXTurn ? "X" : "O";
    setBoard(newBoard);

    const theWinner = checkIsGameOver(newBoard);
    if (theWinner) {
      setGameStatus({ isGameOver: true, winner: theWinner });
      return;
    }

    setIsXTurn((prev) => !prev);
  }

  function handleReset() {
    setBoard(Array(9).fill(""));
    setIsXTurn(true);
    setGameStatus({
      isGameOver: false,
      winner: "",
    });
  }

  function checkIsGameOver(currentBoard) {
    const winners = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];

    for (let i = 0; i < winners.length; i++) {
      const [a, b, c] = winners[i];
      if (
        currentBoard[a] &&
        currentBoard[a] === currentBoard[b] &&
        currentBoard[a] === currentBoard[c]
      ) {
        return currentBoard[a];
      }
    }
    return currentBoard.includes("") ? null : "Draw";
  }
  return (
    <div id="container">
      <h1>Tic Tac Toe</h1>
      <div id="grid">
        {[0, 1, 2].map((row) => (
          <div className="row" key={row}>
            {[0, 1, 2].map((col) => {
              const index = row * 3 + col;
              return (
                <button
                  className="square"
                  key={index}
                  id={index}
                  onClick={handleClick}
                >
                  {board[index]}
                </button>
              );
            })}
          </div>
        ))}
        {gameStatus.isGameOver && (
          <div id="winner-screen">
            <span>
              {gameStatus.winner === "Draw"
                ? "Draw"
                : `Winner: ${gameStatus.winner}`}
            </span>
          </div>
        )}
      </div>

      <button id="reset" onClick={handleReset}>
        Reset Game
      </button>
    </div>
  );
}
