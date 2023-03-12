import pygame
import sys

from const import *
from game import Game
from dragger import Dragger


class Main:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game=Game()
    def mainloop(self):
        game=self.game
        screen=self.screen
        dragger=self.game.dragger
        board=self.game.board
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)
            game.show_moves(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                #click
                if event.type==pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    print(event.pos)

                    clicked_row=dragger.mouseY//SQSIZE
                    clicked_col=dragger.mouseX//SQSIZE
                    
                    
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece=board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece,clicked_col,clicked_row)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        #show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                #mouse motion
                elif event.type==pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                #click release
                elif event.type==pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()
                #quit application
                elif event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            pygame.display.update()

main=Main()
main.mainloop()