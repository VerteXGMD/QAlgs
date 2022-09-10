$$ \lvert \psi_1 \rangle = I^{\otimes n} \lvert 0 \rangle^{\otimes n} X \lvert 0 \rangle =  \lvert 0 \rangle^{\otimes n} \lvert 1 \rangle $$

$$ \lvert \psi_2 \rangle = H^{\otimes (n + 1)} \lvert 0 \rangle^{\otimes n} \lvert 1 \rangle = \lvert + \rangle^{\otimes n} \lvert - \rangle = \frac{1}{\sqrt{2^{n+1}}} \sum_{x = 0}^{2^n - 1} \lvert x \rangle (\lvert 0 \rangle - \lvert 1 \rangle) $$

$$ \lvert \psi_3 \rangle = U_f \frac{1}{\sqrt{2^{n+1}}} \sum_{x = 0}^{2^n - 1} \lvert x \rangle (\lvert 0 \rangle - \lvert 1 \rangle) = \frac{1}{\sqrt{2^{n+1}}} \sum_{x = 0}^{2^n - 1} \lvert x \rangle (\lvert f(x) \rangle - \lvert 1 \oplus f(x) \rangle) $$

$$ \lvert f(x) \rangle - \lvert 1 \oplus f(x) \rangle $$

$$ f(x) = 0 \to \lvert 0 \rangle - \lvert 1 \rangle \\
f(x) = 1 \to \lvert 1 \rangle - \lvert 0 \rangle $$

$$ \psi_3^\prime = (-1)^{f(x)} (\lvert 0 \rangle - \lvert 1 \rangle) $$

$$ \lvert \psi_3 \rangle = \frac{1}{\sqrt{2^{n+1}}} \sum_{x = 0}^{2^n - 1} (-1)^{f(x)} \lvert x \rangle (\lvert 0 \rangle - \lvert 1 \rangle) $$

$$ \lvert \psi_3^\prime \rangle = \frac{1}{\sqrt{2^n}} \sum_{x = 0}^{2^n - 1} (-1)^{f(x)} \lvert x \rangle $$

$$ \lvert \psi_4^\prime \rangle = H^{\otimes n}\frac{1}{\sqrt{2^n}} \sum_{x = 0}^{2^n - 1} (-1)^{f(x)} \lvert x \rangle = \frac{1}{2^n} \sum_{x = 0}^{2^n - 1} \sum_{y = 0}^{2^n - 1} (-1)^{f(x) + x \cdot y} \lvert y \rangle $$
