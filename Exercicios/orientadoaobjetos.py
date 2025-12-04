class Canal:
    def __init__(self, nome, inscritos, descricao):
        self.nome = nome
        self.inscritos = inscritos
        self.descricao = descricao
        self.videos = []
        self.playlists:list[Playlist] = []
   
    def inscrever(self, quantidade=1):
        self.inscritos += quantidade
    def postar(self, video):
        if video in self.videos:
            print(f"O video ja esta no canal.")
            return
        self.videos.append(video)
    def info_play(self):
        for playlist in self.playlists:
            print(playlist.nome)
            playlist.info_videos()
    def criar_playlist(self, playlists):
        if playlists not in self.playlists:
            self.playlists.append(playlists)
        else:
            print("A playlist ja existe no canal.")
    def remover_playlist(self, playlists):
        if playlists in self.playlists:
            self.playlists.remove(playlists)
        else:
            print("A playlist nao existe no canal.")
       

class CanalEmpresa(Canal):
    def __init__(self, nome, inscritos, descricao):
        super().__init__(nome, inscritos, descricao)
        self._equipe = []
    
    @property
    def equipe(self):
        return self._equipe
    
    def adicionar_membro(self,membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print(f"{membro} já faz parte da equipe.")

    def remover_membro(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print(f"{membro} não faz parte da equipe de {self.nome}.")

class Video:
    
    def __init__(self, titulo, descricao ):
        self.titulo = titulo
        self.descricao = descricao
        self.comentarios = []
        self.visualizacoes = 0
        self.likes = 0
        self.dislikes = 0

    def __repr__(self):
        return f"<{self.titulo}>"
    
    def visualizar(self):
        self.visualizacoes += 1

    def like(self):
        self.likes += 1

    def dislike(self):
        self.dislikes += 1

    def adicionar_comentario(self, comentario):
        self.comentarios.append(comentario)

    def informacoes(self):
        print(f"""Titulo: {self.titulo}
            descricao: {self.descricao}
            visualizacoes: {self.visualizacoes}
            likes: {self.likes}
            dislikes: {self.dislikes}
            comentarios: {self.comentarios}
            /n""")
        
class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.videos:list[Video] = []
    def adicionar_video(self,video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print(f"O video ja esta na playlist.")
    def remover_video(self,video):
        if video in self.videos:
            self.videos.remove(video)
        else:
            print(f"O video nao esta na playlist.")
    def info_videos(self):
        for video in self.videos:
            video.informacoes()

        

canal_python = Canal("Curso em video", 1000000, "Canal de tecnologia")
canal_Gustavo = Canal("Gustavo7612", 385, "Canal de games")
canal_duolingo = CanalEmpresa("Duolingo", 500000,"Canal de idiomas")
video_aula = Video("Aula de python", "Introducao a ML")
video_discord = Video("Configurando bot discord", "Passo a passo para configurar um bot no discord")
playlist_projetos = Playlist("Projetos Python")
playlist_projetos.adicionar_video(video_aula)
playlist_projetos.adicionar_video(video_discord)
video_valorant = Video("CLipes valorant", "CLipes insanos de valorant")
playlist_fps = Playlist("Jogos FPS")
playlist_fps.adicionar_video(video_valorant)
canal_Gustavo.criar_playlist(playlist_projetos)
canal_Gustavo.criar_playlist(playlist_fps)

canal_Gustavo.info_play()

print(f"{canal_Gustavo.nome} tem {canal_Gustavo.inscritos} inscritos.")
canal_Gustavo.inscrever(15)
print(f"{canal_Gustavo.nome} agora tem {canal_Gustavo.inscritos} inscritos.")
print(f"Membros da equipe do canal {canal_duolingo.nome}: {canal_duolingo.equipe}")
canal_duolingo.adicionar_membro("Ana")
print(f"Membros da equipe do canal {canal_duolingo.nome}: {canal_duolingo.equipe}")  

canal_Gustavo.postar(video_aula)
canal_Gustavo.postar(video_discord)
print(canal_Gustavo.videos)