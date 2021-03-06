import unittest
from potion_trading import best_trades

class MyTestCase(unittest.TestCase):
    def test_best_trades_1(self):
        prices = [10, 5, 1, 0.1]
        starting_liquid = 0
        max_trades = 6
        townspeople = [[(0, 1, 4), (2, 3, 30)], [(1, 2, 2.5), (2, 0, 0.2)]]
        v1 = best_trades(prices, starting_liquid, max_trades, townspeople)
        max_trades = 2
        v2 = best_trades(prices, starting_liquid, max_trades, townspeople)
        assert ( v1 == 60 and v2 == 20 ) , "Failed given examples in assignment sheet for best_trades"

    def test_large_set_best_trades(self):
        liquids = [2.0, 1.3, 1.9, 0.3, 1.2, 0.5, 1.1, 1.5, 1.1, 1.6, 0.2, 0.5, 1.7, 1.7, 0.6, 1.7, 0.8, 0.8, 1.5, 2.0,
                   0.8, 0.3, 1.2, 1.0, 0.6, 0.5, 1.4, 1.9, 1.2, 1.7, 1.9, 0.7, 0.5, 1.2, 0.2, 1.3, 1.7, 0.9, 0.7, 1.8,
                   0.7, 1.9, 0.3, 1.1, 1.4, 0.6, 1.5, 1.7, 0.6, 0.5, 1.1, 0.3, 2.0, 0.6, 0.2, 1.1, 1.0, 0.8, 0.4, 1.1,
                   0.4, 0.4, 1.3, 2.0, 1.0, 0.5, 1.8, 1.7, 1.3, 1.4, 1.8, 0.6, 1.3, 1.9, 0.3, 0.9, 1.0, 0.7, 1.3, 0.6,
                   1.3, 1.0, 1.1, 0.3, 0.4, 1.4, 0.1, 1.1, 0.5, 1.4, 0.5, 0.8, 1.9, 1.5, 2.0, 0.9, 1.5, 1.4, 1.5, 1.1]
        townspeople = [[(40, 95, 1.558)],
                       [(27, 1, 1.634), (26, 77, 1.294), (41, 44, 1.928), (64, 16, 0.3), (29, 52, 0.198),
                        (74, 17, 0.468), (59, 12, 1.558), (55, 91, 1.486)],
                       [(35, 30, 1.012), (89, 11, 0.954), (95, 47, 1.34), (57, 28, 0.224), (93, 31, 0.87),
                        (49, 89, 1.16), (99, 2, 0.078), (42, 63, 1.416), (21, 46, 1.358), (85, 6, 0.922)],
                       [(11, 21, 1.304), (81, 92, 1.298), (70, 57, 1.74), (96, 7, 0.96), (38, 23, 1.516),
                        (8, 14, 1.034), (6, 79, 1.056), (25, 64, 1.318)],
                       [(48, 84, 1.438), (45, 96, 1.058), (80, 59, 1.754), (97, 67, 1.368), (46, 42, 0.406),
                        (16, 66, 1.386), (78, 76, 0.614)],
                       [(56, 99, 0.696), (3, 86, 0.01), (72, 75, 0.152), (5, 88, 1.16), (77, 82, 1.568)],
                       [(65, 24, 1.586), (75, 3, 1.662)], [(67, 58, 1.744), (50, 5, 1.438)],
                       [(94, 4, 0.488), (47, 13, 0.396), (76, 50, 0.654)],
                       [(68, 97, 0.628), (71, 94, 1.356), (90, 68, 1.682), (84, 43, 0.546)],
                       [(92, 27, 1.936), (87, 53, 0.348), (10, 69, 1.234), (63, 56, 0.086), (83, 74, 1.804)],
                       [(14, 80, 1.314), (32, 29, 1.162), (4, 87, 0.302), (1, 98, 0.384), (37, 32, 0.374),
                        (12, 35, 1.9)], [(91, 25, 1.164)],
                       [(30, 61, 0.426), (52, 65, 1.54), (24, 18, 1.052), (98, 37, 1.834), (73, 33, 1.302),
                        (28, 83, 0.48), (69, 48, 0.824), (66, 34, 0.766)],
                       [(13, 93, 1.332), (22, 51, 1.05), (53, 60, 0.236), (23, 72, 1.08), (20, 81, 1.54),
                        (82, 38, 1.144), (62, 54, 0.462), (36, 26, 1.85)],
                       [(17, 0, 1.362), (79, 39, 1.46), (33, 70, 0.636), (15, 90, 1.906), (86, 41, 1.918),
                        (58, 62, 0.016), (43, 85, 1.442), (7, 9, 0.39), (60, 8, 0.876)],
                       [(0, 73, 1.578), (39, 78, 0.246)],
                       [(9, 36, 1.17), (44, 19, 1.926), (19, 55, 1.472), (18, 15, 1.92), (31, 49, 0.104), (2, 20, 0.59),
                        (34, 10, 0.918), (54, 40, 0.856)], [(61, 22, 1.348)], [(88, 71, 0.966), (51, 45, 0.592)],
                       [(37, 30, 0.154)],
                       [(39, 15, 0.634), (26, 4, 1.008), (86, 11, 0.764), (30, 36, 0.68), (14, 21, 0.864)],
                       [(37, 10, 0.94), (79, 79, 1.226), (66, 90, 1.5)],
                       [(27, 81, 1.334), (62, 97, 1.158), (68, 74, 1.228), (93, 55, 0.006)],
                       [(81, 56, 0.3), (50, 6, 0.966), (75, 99, 0.95), (41, 33, 1.546), (74, 91, 0.162), (79, 85, 0.39),
                        (67, 35, 0.204), (77, 62, 0.608)],
                       [(75, 44, 1.41), (83, 26, 0.074), (57, 37, 1.842), (64, 67, 1.196), (22, 18, 0.176),
                        (71, 94, 1.53), (32, 0, 0.894), (88, 45, 1.154), (37, 45, 0.184)],
                       [(66, 19, 1.782), (50, 93, 1.914), (7, 93, 0.086), (85, 91, 1.8), (95, 97, 0.196),
                        (51, 68, 0.988), (1, 2, 0.428), (90, 55, 1.144), (97, 6, 0.034)],
                       [(93, 54, 1.36), (26, 82, 0.24), (1, 16, 0.834)],
                       [(85, 59, 0.846), (35, 95, 0.764), (24, 62, 0.132), (6, 73, 1.046), (42, 46, 0.102),
                        (25, 13, 1.586), (12, 31, 0.804)],
                       [(23, 71, 1.864), (23, 35, 0.996), (17, 6, 1.684), (70, 45, 1.768), (66, 13, 1.294),
                        (50, 80, 1.032), (62, 25, 0.248), (32, 52, 1.244), (68, 56, 1.124)],
                       [(16, 44, 1.226), (45, 48, 0.426)],
                       [(57, 15, 0.79), (93, 43, 0.83), (70, 2, 0.282), (84, 7, 1.44), (76, 80, 0.794), (59, 49, 0.962),
                        (29, 53, 1.504), (37, 31, 1.928), (88, 93, 1.674)],
                       [(44, 78, 0.864), (91, 60, 0.136), (50, 89, 1.074), (61, 70, 0.136), (76, 97, 1.492),
                        (59, 40, 1.418), (47, 56, 0.776), (90, 66, 1.68), (88, 75, 0.264), (96, 48, 1.162)],
                       [(97, 26, 1.28), (39, 56, 1.956), (46, 21, 0.524), (12, 78, 1.188), (27, 51, 0.956),
                        (19, 82, 0.296)], [(53, 20, 0.47), (5, 54, 1.496), (1, 90, 1.188), (5, 93, 0.2)],
                       [(76, 85, 1.598), (47, 76, 0.26), (74, 62, 1.022), (35, 96, 1.756)],
                       [(66, 51, 1.712), (19, 77, 0.562), (5, 62, 1.512), (24, 40, 0.268), (93, 27, 0.768)],
                       [(59, 77, 1.166), (15, 58, 0.756), (41, 57, 1.25), (30, 95, 0.326), (11, 23, 1.008),
                        (90, 58, 0.424), (99, 41, 1.674), (70, 78, 1.3), (32, 9, 1.332)],
                       [(99, 34, 1.626), (28, 67, 0.164), (3, 99, 1.392), (44, 79, 0.072), (11, 2, 0.126),
                        (56, 83, 0.03), (12, 6, 1.044), (73, 45, 1.268), (24, 9, 0.906), (20, 59, 0.992)],
                       [(3, 29, 0.968)],
                       [(44, 81, 1.948), (2, 24, 0.562), (16, 74, 0.94), (75, 66, 1.24), (20, 10, 1.022),
                        (74, 40, 0.704)],
                       [(8, 53, 1.638), (59, 65, 0.638), (83, 99, 0.378), (70, 57, 0.828), (98, 43, 0.658),
                        (68, 51, 0.316)],
                       [(40, 13, 1.38), (85, 24, 0.26), (71, 88, 0.112), (59, 21, 1.036), (40, 69, 1.686),
                        (88, 99, 1.518), (35, 97, 0.544), (78, 74, 0.6)],
                       [(75, 83, 0.804), (91, 95, 0.48), (22, 60, 1.646)],
                       [(70, 90, 1.618), (31, 72, 1.878), (43, 17, 1.202)],
                       [(59, 18, 1.886), (66, 25, 0.562), (91, 47, 1.482), (38, 6, 0.416)],
                       [(58, 95, 0.28), (83, 99, 1.86), (27, 89, 0.52)],
                       [(36, 50, 1.282), (14, 39, 1.93), (29, 8, 1.808), (99, 49, 1.56), (69, 0, 0.57),
                        (50, 43, 1.304)],
                       [(13, 30, 1.782), (27, 88, 0.834), (57, 97, 0.864), (57, 23, 1.594), (55, 8, 1.946)],
                       [(69, 64, 1.46), (91, 16, 1.296), (25, 62, 0.186), (22, 82, 0.806), (39, 51, 1.896),
                        (40, 40, 1.228), (51, 86, 0.99), (43, 32, 0.454)],
                       [(99, 5, 1.126), (59, 81, 0.762), (72, 52, 0.998), (47, 67, 0.298), (32, 58, 1.46),
                        (46, 12, 0.572)],
                       [(90, 44, 0.81), (93, 11, 0.922), (41, 39, 1.678), (15, 61, 1.692), (94, 70, 0.648),
                        (68, 30, 1.84)],
                       [(7, 96, 1.938), (8, 30, 0.964), (57, 8, 1.048), (60, 7, 1.728), (57, 67, 1.534),
                        (84, 8, 0.876)], [(38, 59, 0.466), (33, 63, 0.894)],
                       [(86, 99, 1.188), (3, 8, 0.668), (91, 68, 0.266), (12, 26, 0.524)],
                       [(76, 26, 0.092), (75, 3, 1.396), (47, 75, 0.974), (11, 69, 0.61), (16, 66, 2.0), (33, 43, 0.64),
                        (83, 21, 0.086), (62, 5, 1.226), (91, 51, 0.864), (42, 11, 1.06)],
                       [(66, 69, 1.016), (59, 75, 1.194), (19, 53, 1.986), (43, 38, 0.636), (51, 74, 0.882),
                        (30, 72, 0.438), (37, 66, 0.734), (22, 84, 1.072), (96, 3, 0.082), (64, 45, 0.264)],
                       [(19, 96, 0.364), (99, 85, 1.834), (18, 48, 1.206), (77, 39, 0.244), (98, 4, 0.756),
                        (42, 72, 1.484), (85, 83, 1.892), (85, 40, 0.342)],
                       [(77, 14, 1.194), (72, 67, 1.884), (68, 21, 0.65), (56, 80, 1.144), (95, 28, 0.494),
                        (5, 41, 1.488), (80, 0, 0.744), (96, 25, 1.202), (6, 72, 1.432)],
                       [(25, 87, 0.424), (90, 6, 0.856), (45, 64, 0.008), (8, 50, 0.844), (85, 81, 0.548),
                        (96, 13, 0.062), (51, 36, 1.018), (19, 6, 0.392)],
                       [(57, 24, 0.454), (50, 44, 0.176), (82, 62, 0.912)],
                       [(22, 77, 0.398), (86, 76, 1.002), (61, 78, 1.802), (76, 50, 1.42), (15, 51, 1.322),
                        (17, 33, 1.852)],
                       [(88, 97, 1.494), (91, 99, 1.718), (62, 18, 1.476), (67, 48, 1.554), (22, 25, 1.51),
                        (6, 86, 1.642), (0, 61, 0.092), (40, 80, 0.616)],
                       [(67, 19, 1.342), (66, 61, 1.828), (24, 48, 0.226), (78, 4, 0.12), (38, 58, 1.574)],
                       [(29, 25, 1.066), (87, 77, 0.474), (49, 10, 1.414), (89, 48, 1.974), (31, 10, 0.336)],
                       [(54, 12, 0.872), (97, 73, 0.362), (99, 20, 0.266), (29, 39, 1.422), (91, 5, 0.034),
                        (41, 38, 1.872), (52, 51, 1.904), (70, 53, 1.19)],
                       [(75, 44, 1.806), (21, 29, 1.106), (17, 67, 0.624), (25, 58, 1.296), (96, 13, 1.624),
                        (60, 70, 1.154), (29, 59, 1.902)], [(98, 83, 0.3), (80, 77, 0.96), (20, 45, 1.092)],
                       [(35, 29, 1.708), (8, 7, 0.73)],
                       [(34, 35, 0.99), (62, 97, 1.566), (1, 25, 0.206), (56, 62, 0.472), (86, 2, 1.926),
                        (87, 20, 1.974), (27, 5, 1.198)],
                       [(32, 74, 0.666), (84, 94, 1.284), (50, 96, 1.576), (14, 61, 0.574), (97, 3, 1.348)],
                       [(39, 61, 0.618), (34, 44, 1.762), (18, 77, 0.86)],
                       [(72, 86, 0.33), (52, 54, 0.626), (11, 16, 1.654), (95, 93, 0.64), (42, 19, 0.578),
                        (34, 90, 1.838), (35, 84, 1.884), (49, 91, 0.182), (55, 79, 1.968)],
                       [(97, 95, 1.448), (29, 95, 1.932), (39, 81, 1.942), (94, 79, 1.258), (93, 80, 1.974),
                        (56, 79, 0.052), (99, 88, 0.986), (14, 56, 1.876), (88, 6, 0.32)],
                       [(67, 86, 0.328), (88, 98, 0.812), (73, 76, 0.004), (8, 86, 1.542), (48, 37, 0.496),
                        (41, 63, 0.974), (24, 72, 0.854)],
                       [(27, 64, 0.564), (93, 49, 1.602), (42, 40, 0.604), (11, 83, 0.238), (92, 13, 1.778),
                        (31, 62, 0.942), (53, 14, 1.37), (38, 18, 1.982), (13, 74, 0.292)],
                       [(74, 92, 1.024), (81, 15, 0.28), (78, 68, 1.91), (45, 67, 1.042), (43, 27, 1.552),
                        (26, 97, 1.212), (68, 87, 0.078)],
                       [(61, 57, 0.126), (92, 66, 1.162), (33, 37, 0.11), (4, 90, 0.586), (46, 44, 0.344),
                        (97, 7, 1.06), (11, 32, 0.586), (22, 5, 0.192), (5, 71, 0.8)],
                       [(72, 21, 1.586), (43, 59, 1.248), (58, 39, 0.726), (31, 49, 0.54)],
                       [(45, 48, 0.564), (17, 20, 1.998)],
                       [(84, 62, 0.964), (56, 37, 0.006), (45, 71, 0.046), (94, 95, 0.708)],
                       [(3, 11, 0.952), (66, 20, 1.826), (87, 90, 0.194), (29, 51, 1.592)],
                       [(75, 17, 0.004), (45, 57, 0.43), (86, 84, 0.424), (6, 44, 1.73), (70, 97, 0.81),
                        (69, 94, 0.39)],
                       [(26, 73, 1.838), (8, 6, 0.476), (12, 58, 1.134), (86, 32, 1.264), (31, 59, 1.154),
                        (91, 42, 0.212), (14, 65, 0.606)], [(96, 36, 1.454)], [(98, 21, 0.738), (49, 53, 1.504)],
                       [(13, 71, 1.832), (63, 96, 0.8), (8, 70, 0.888), (58, 39, 0.31), (48, 77, 1.104),
                        (87, 99, 1.922), (4, 48, 1.176)],
                       [(77, 30, 1.222), (4, 33, 1.262), (3, 50, 1.232), (91, 6, 1.622), (60, 4, 0.63), (35, 13, 0.936),
                        (4, 87, 0.362), (44, 82, 1.494), (69, 47, 0.664)], [(44, 3, 1.09), (4, 96, 1.78)],
                       [(63, 58, 1.772), (75, 8, 0.558), (82, 79, 1.436), (46, 31, 0.072), (41, 35, 1.262)],
                       [(45, 99, 1.9), (66, 76, 1.288), (3, 32, 1.832), (43, 94, 1.724), (75, 43, 1.9), (65, 26, 0.62),
                        (70, 33, 0.976), (39, 56, 1.796), (2, 63, 0.842)],
                       [(40, 46, 1.97), (42, 25, 0.752), (74, 99, 0.438), (50, 11, 1.316), (38, 49, 0.068),
                        (54, 38, 1.438)], [(55, 90, 0.086), (48, 77, 1.488), (58, 80, 1.14)],
                       [(59, 82, 0.12), (85, 46, 1.944), (73, 88, 1.31), (23, 86, 1.412), (68, 27, 1.454),
                        (15, 25, 0.54), (66, 44, 0.24)], [(85, 62, 0.838)], [(71, 16, 0.26), (43, 94, 0.018)],
                       [(31, 83, 1.758)],
                       [(75, 59, 1.064), (12, 97, 1.43), (87, 15, 1.59), (15, 20, 0.704), (30, 52, 1.236),
                        (23, 88, 0.986), (83, 17, 0.25)],
                       [(17, 21, 1.048), (25, 7, 1.31), (44, 43, 0.004), (9, 15, 0.82), (25, 52, 0.872),
                        (97, 88, 1.828), (49, 76, 1.756), (81, 29, 0.434), (12, 24, 0.194)],
                       [(64, 79, 1.608), (27, 84, 0.73), (52, 88, 1.256)]]
        ans = [(22, 78, 1014921803161147146240), (42, 105, 14402401031995342596937351168),
               (91, 114, 9213370577561810566532244176896), (43, 20, 331227), (59, 105, 22544473029519326673427759104),
               (29, 155, 773597304046763012932208871477550382055424), (20, 83, 29322000651282697682944), (25, 4, 14),
               (60, 107, 77328008882992225759642255360), (96, 108, 133186311173754327558271270912),
               (32, 59, 5496955320652260), (14, 157, 1823556588693798857749618843345961961390080),
               (1, 148, 5449941364461770773498490038288432234496),
               (36, 181, 9512101886108196421384222382302390605618052333568), (72, 99, 395173728351163660573343744),
               (99, 37, 17067508448), (38, 46, 2998221557730), (58, 39, 21219540649),
               (19, 147, 5390992139953547595469331062601031876608), (1, 125, 3602918130030602145394246887145472),
               (51, 200, 699881827500142315607304139842779969877000880327229440), (42, 92, 3929187274255377545297920),
               (36, 27, 22273232), (13, 11, 1176), (42, 185, 50019386988932095865478581460517510310984943665152),
               (14, 144, 584010843904099164132762379775371116544), (11, 119, 143359790259947418893767982186496),
               (9, 142, 154752827477416194887058444771013951488), (71, 45, 654479270505),
               (27, 97, 98314101663951058318131200), (75, 47, 6854722522358),
               (35, 173, 47981457356225439367431640006332910668009701376),
               (83, 142, 413426638527209735139917481672718680064),
               (41, 194, 29245464082242745548222686216932663747808137393995776),
               (46, 143, 132582442241677779723289862404176871424), (30, 98, 174853695749727611443478528),
               (73, 45, 1712812391400), (87, 113, 5777749388302320220098558689280), (39, 37, 6478575319),
               (66, 149, 17623798349748284206927394509934531969024),
               (26, 172, 32438325188007458914022012615917222108030042112), (92, 84, 38461688368486068256768),
               (92, 181, 6740418345222813489904116985913480823701822767104), (60, 13, 3405), (68, 44, 477640603962),
               (60, 158, 4523814176112568669143503562151288182407168), (25, 15, 9509),
               (66, 101, 1944307686650017035990335488), (3, 34, 2170311507),
               (83, 127, 36917426441924210395606746795081728), (69, 114, 2418267607026890708287576080384),
               (70, 173, 93638715999564990890884658500060729724454830080),
               (18, 131, 232273181395292077068047327330041856),
               (59, 174, 95325362059344869714056242489606438538589503488), (90, 115, 11280743649372796493862163972096),
               (46, 7, 31), (27, 72, 17489421015780265984), (25, 170, 5877309060066749427355559294135165499117404160),
               (52, 11, 987), (93, 60, 19514995108872868), (75, 79, 3271172767948688326656), (48, 13, 2216),
               (14, 24, 2360938), (62, 11, 1223), (44, 93, 12892412152573519930064896), (50, 56, 1599681889821685),
               (49, 11, 1344), (84, 102, 2466412402878834043334426624),
               (94, 136, 3052460394791196695459796699892940800),
               (20, 195, 45759741446455451904724543332497619902536985083904000),
               (4, 179, 1788290342654266861874238491785044662852660494336), (22, 33, 722655759),
               (41, 89, 1324003858470312425291776), (16, 79, 2570736434072087691264),
               (91, 105, 34270332392466489335959519232), (40, 5, 18), (87, 41, 211717578152),
               (3, 197, 198143561778485089583901531759136217995255325483073536), (53, 20, 150254),
               (4, 122, 733843220612427283789242557267968), (14, 8, 170), (22, 41, 108903447399), (43, 37, 13419491375),
               (25, 162, 39000337841531187479402132555100246278930432),
               (33, 181, 4207588522741200039770381884466341833811563642880), (46, 101, 609281944004056001231716352),
               (75, 115, 17088516950386553019572177338368), (44, 42, 220376992212), (23, 78, 968834189542678593536),
               (89, 129, 44960222771300288900888553288892416), (4, 114, 5822272489312545569382537887744),
               (58, 66, 412322131989543168), (93, 20, 341256), (88, 20, 358461),
               (10, 190, 525599215856254519755444538085187405497733673385984),
               (4, 142, 191887673178051077212454827951852093440), (34, 90, 2040009878342187857477632),
               (94, 116, 11673638696045614001448315518976), (56, 91, 2644398013243021462601728),
               (81, 116, 13354467539759263516808863285248)]

        all_pass = True
        fail_at = []
        for a in ans:
            if best_trades(liquids , a[0]  ,a[1] , townspeople) != a[2]:
                fail_at.append(a)
                all_pass = False

        print(fail_at)
        assert all_pass , str(len(fail_at)) + " Failed tests for the following where format is (start , max_trades, expected_value)" + "\n" + str(fail_at)

if __name__ == '__main__':
    unittest.main()