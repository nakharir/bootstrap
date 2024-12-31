class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = {}

    def add_rule(self, condition, conclusion):
        self.rules.append((condition, conclusion))

    def add_fact(self, fact_name, value):
        self.facts[fact_name] = value

    def evaluate_rules(self):
        recommendations = []
        for condition, conclusion in self.rules:
            if all(self.facts.get(cond, False) for cond in condition):
                recommendations.append(conclusion)
        return recommendations

def main():
    # Inisialisasi sistem pakar
    expert_system = ExpertSystem()

    # Menambahkan aturan
    expert_system.add_rule(('A', 'C'), 'Samsung')  # R1: Jika memiliki uang 2 jt dan memilih TV dengan internet, maka rekomendasi Samsung
    expert_system.add_rule(('D', 'C'), 'LG')       # R2: Jika memilih TV ber Android dan memiliki internet, maka rekomendasi LG
    expert_system.add_rule(('B', 'C'), 'LG')       # R3: Jika memiliki uang 4 jt dan memilih TV dengan internet, maka rekomendasi LG
    expert_system.add_rule(('B',), 'Samsung')       # R4: Jika memiliki uang 4 jt, maka rekomendasi Samsung
    expert_system.add_rule(('D',), 'Panasonic')     # R5: Jika memilih TV ber Android, maka rekomendasi Panasonic

    # Input dari pengguna
    print("Pilih jumlah uang yang Anda miliki:")
    print("1. 2 juta")
    print("2. 4 juta")
    uang_choice = input("Masukkan pilihan (1/2): ").strip()

    if uang_choice == '1':
        expert_system.add_fact('A', True)  # Memiliki uang 2 juta
        expert_system.add_fact('B', False)  # Tidak memiliki uang 4 juta
    elif uang_choice == '2':
        expert_system.add_fact('A', False)  # Tidak memiliki uang 2 juta
        expert_system.add_fact('B', True)   # Memiliki uang 4 juta
    else:
        print("Pilihan tidak valid.")
        return

    print("\nPilih jenis TV yang Anda inginkan:")
    print("1. Memiliki fitur internet")
    print("2. TV ber Android")
    tv_choice = input("Masukkan pilihan (1/2): ").strip()

    if tv_choice == '1':
        expert_system.add_fact('C', True)   # Memilih TV yang memiliki fitur internet
        expert_system.add_fact('D', False)  # Tidak memilih TV ber Android
    elif tv_choice == '2':
        expert_system.add_fact('C', False)  # Tidak memilih TV yang memiliki fitur internet
        expert_system.add_fact('D', True)   # Memilih TV ber Android
    else:
        print("Pilihan tidak valid.")
        return

    # Evaluasi aturan
    recommendations = expert_system.evaluate_rules()

    # Menampilkan rekomendasi
    if recommendations:
        print("\nRekomendasi TV yang dapat dibeli:")
        for rec in recommendations:
            print(rec)
    else:
        print("Tidak ada rekomendasi yang sesuai.")

if __name__ == "__main__":
    main()