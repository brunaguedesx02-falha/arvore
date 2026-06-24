class Node:
    def __init__(self, content):
        self.left:Node = None   
        self.right:Node = None
        self.content:str = content  
    
class Tree:
    def __init__(self):
        self.root:Node = None
    
    def add(self, content, root = None):
        if self.root is None:
            self.root = Node(content)
            return
        
        if root is None:
            root = self.root
        
        if content > root.content:
            if (root.right is None):
                root.right = Node(content)
            else:
                self.add(content, root.right)
        
        else:
            if (root.left is None):
                root.left = Node(content)
            else:
                self.add(content, root.left)
    
    def printTreeInOrd(self, root = None):
        if root is None:
            root = self.root
        
        if root:
            if root.left:
                self.printTreeInOrd(root.left)
            
            print(f" 🐾 {root.content}")
            
            if root.right:
                self.printTreeInOrd(root.right)

    def printPreOrder(self, root=None):
        """Raiz -> Esquerda -> Direita"""
        if root is None:
            root = self.root
            
        if root:
            print(root.content)
            if root.left: self.printPreOrder(root.left)
            if root.right: self.printPreOrder(root.right)

    def printPostOrder(self, root=None):
        """Esquerda -> Direita -> Raiz"""
        if root is None:
            root = self.root
            
        if root:
            if root.left: self.printPostOrder(root.left)
            if root.right: self.printPostOrder(root.right)
            print(root.content)

    def remove(self, content, root = None):
        if self.root is None:
            return None
        if root is None:
            self.root = self._removeNode(self.root, content)
        else:
            root = self._removeNode(root, content)

    def _removeNode(self, root, content):
        if root is None:
            return root
            
        if content < root.content:
            root.left = self._removeNode(root.left, content)
        elif content > root.content:
            root.right = self._removeNode(root.right, content)
        else:
            # === CASO 1: O paciente é um nó FOLHA (Sem animais abaixo dele) ===
            if root.left is None and root.right is None:
                return None
                
            # === CASO 2: O paciente só tem 1 animal abaixo dele ===
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
                
            else:
            # === CASO 3: O paciente tem 2 animais abaixo dele ===
                temp = self._minValueNode(root.right)
                root.content = temp.content
                root.right = self._removeNode(root.right, temp.content)
                
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, content, root = None):
        if self.root is None:
            return False
        if root is None:
            root = self.root
            
        if root is None: 
            return False
        if root.content == content:
            return True
            
        if content < root.content:
            if root.left is None: return False
            return self.search(content, root.left)
            
        if root.right is None: return False
        return self.search(content, root.right)

def iniciar_sistema():
    sala_espera = Tree()
    
    # Pacientes iniciais do dia
    sala_espera.add("Mel")
    sala_espera.add("Thor")
    sala_espera.add("Bidu")
    
    fim_de_jogo = False
    
    print("\n====================================================")
    print("        SISTEMA DE GESTÃO VETERINÁRIA   🏥        ")
    print("====================================================")
    print("Olá, Doutor(a)! O sistema da recepção já está online.")
    print("Temos alguns pacientes aguardando atendimento na recepção.\n")

    while not fim_de_jogo:
        print("\n--- PAINEL DE CONTROLE DA CLÍNICA ---")
        print("1. Chamar paciente para o consultório")
        print("2. Visualizar lista de pacientes na recepção")
        print("3. Registrar chegada de novo paciente")
        print("4. Encerrar expediente (Fechar sistema)")
        
        escolha = input("Selecione a ação desejada (1-4): ")

        if escolha == "1":
            print("\n[CHAMAR PACIENTE]")
            pet = input("Digite o nome do pet que vai ser atendido agora: ")
            pet_ajustado = pet.capitalize()
            
            if sala_espera.search(pet_ajustado):
                sala_espera.remove(pet_ajustado)
                print(f"🩺 [SALA 01]: O pet '{pet_ajustado}' deu entrada no consultório.")
            else:
                print(f"❌ Erro: '{pet_ajustado}' não consta na lista de presença da recepção.")

        elif escolha == "2":
            print("\n=== PACIENTES AGUARDANDO NA RECEPÇÃO ===")
            if sala_espera.root is None:
                print("Nenhum animal aguardando no momento. Todos os atendimentos concluídos!")
            else:
                sala_espera.printTreeInOrd()
            print("==========================================")

        elif escolha == "3":
            print("\n[REGISTRAR CHEGADA]")
            novo_pet = input("Digite o nome do animal que acabou de chegar: ")
            novo_pet_ajustado = novo_pet.capitalize()
            
            sala_espera.add(novo_pet_ajustado)
            print(f"📝 Confirmado: '{novo_pet_ajustado}' recebeu a ficha e aguarda na recepção.")

        elif escolha == "4":
            print("Expediente encerrado com sucesso. Até amanhã, Doutor(a)!")
            fim_de_jogo = True
            
        else:
            print("\n⚠️ Comando inválido no teclado do sistema.")

if __name__ == "__main__":
    iniciar_sistema()