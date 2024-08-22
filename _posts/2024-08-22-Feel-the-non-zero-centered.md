---
title: Feel the Non-Zero Centered Problem
date: 2024-08-22
categories: machine-learning
---

<div id="game-container">
  <!-- HTML 요소들 -->

<style>
      body {
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #fff;
      }
      canvas {
        display: block;
      }
</style>

<script src="https://cdn.jsdelivr.net/npm/phaser@3.55.2/dist/phaser.js"></script>

    <script>
      const config = {
        type: Phaser.AUTO,
        width: 800,
        height: 600,
        backgroundColor: "#ffffff",
        scene: {
          preload: preload,
          create: create,
          update: update,
        },
      };

      const startPos = { x: 50, y: 50 };
      const targetPos = { x: 750, y: 550 };
      const speed = 2; // 움직임 속도

      let player;
      let target;
      let pathGraphics;
      let goalReached = false;
      let startTime;
      let elapsedTime = 0;
      let timeText;
      let path = [];
      let instructionsText;
      let waitingForStart = true;
      let cursors;

      const game = new Phaser.Game(config);

      function preload() {
        // 필요한 리소스를 로드하는 곳입니다.
      }

      function create() {
        // 설명서 추가
        instructionsText = this.add
          .text(
            400,
            300,
            "목표: 빨간 공에 도달하세요.\n\n입력키의 부호가 같은 방향으로만 움직일 수 있습니다.\n\n오른쪽 위로 이동, 왼쪽 아래로 이동.\n\n시작하려면 아무 키나 누르세요.",
            {
              fontSize: "24px",
              fill: "#000000",
              align: "center",
            }
          )
          .setOrigin(0.5);

        // 키 입력 대기
        this.input.keyboard.on("keydown", startGame, this);
        cursors = this.input.keyboard.createCursorKeys(); // 방향키 입력 받기
      }

      function startGame() {
        if (waitingForStart) {
          waitingForStart = false;

          // 설명서 제거
          instructionsText.setVisible(false);

          // 게임 초기 설정
          player = this.add.circle(startPos.x, startPos.y, 10, 0x000000);
          target = this.add.circle(targetPos.x, targetPos.y, 10, 0xff0000);
          pathGraphics = this.add.graphics({
            lineStyle: { width: 5, color: 0x0000ff },
          });
          startTime = Date.now();
          timeText = this.add.text(10, 10, "시간: 0초", {
            fontSize: "28px",
            fill: "#000000",
          });

          path.push({ x: player.x, y: player.y });
        }
      }

      function update() {
        if (!waitingForStart && !goalReached) {
          elapsedTime = (Date.now() - startTime) / 1000;
          timeText.setText(`시간: ${elapsedTime.toFixed(2)}초`);

          pathGraphics.clear();
          for (let i = 1; i < path.length; i++) {
            pathGraphics.strokeLineShape(
              new Phaser.Geom.Line(
                path[i - 1].x,
                path[i - 1].y,
                path[i].x,
                path[i].y
              )
            );
          }

          let moved = false;

          if (cursors.right.isDown && cursors.up.isDown) {
            player.x += speed * 1.5;
            player.y -= speed;
            moved = true;
          } else if (cursors.left.isDown && cursors.down.isDown) {
            player.x -= speed;
            player.y += speed * 1.5;
            moved = true;
          } else if (cursors.left.isDown && cursors.up.isDown) {
            player.x -= speed * 0.3;
            player.y -= speed;
            moved = true;
          }

          if (moved) {
            path.push({ x: player.x, y: player.y });
          }

          if (
            Phaser.Math.Distance.Between(
              player.x,
              player.y,
              target.x,
              target.y
            ) < 10
          ) {
            goalReached = true;
            this.add
              .text(400, 300, "목표 지점에 도달했습니다!", {
                fontSize: "40px",
                fill: "#ff0000",
              })
              .setOrigin(0.5);
            this.add
              .text(400, 350, `소요 시간: ${elapsedTime.toFixed(2)}초`, {
                fontSize: "28px",
                fill: "#ff0000",
              })
              .setOrigin(0.5);
            this.add
              .text(400, 400, "다시 시작하려면 F5를 누르세요.", {
                fontSize: "28px",
                fill: "#ff0000",
              })
              .setOrigin(0.5);
          }
        }
      }

  </script>

    <canvas id="gameCanvas"></canvas>

</div>
