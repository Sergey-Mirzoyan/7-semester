clear, clc
 
% параметры распределения:
k = input("k = ");
lambda = input("lambda = ");
step = input("step = ");
% интервал по х:
a = input("a = "); % нижний предел
b = input("b = "); % верхний предел
x = linspace(a,b,step); % разбиваем диапазон на step точек
% формула плотности распределения СВ
w = @(x) lambda.^k * x.^(k-1) .* exp((-1)*lambda*x)/(factorial(k-1));
W = w(x); % считаем плотность
mW = max(W); % находим макс. значение

%Функция распределения СВ
for i=x
    if i >= 0
        WW = 1 - exp(-lambda*x)
    else
        WW = 0
    end
end


% рисуем:
grid on 
subplot(4, 1, 1)
plot(x, pdf('Uniform', x, a, b));
subplot(4, 1, 2);
plot(x, cdf('Uniform', x, a, b));

subplot(4, 1, 3);

plot(x,W,'r');
subplot(4, 1, 4);
plot(x, WW, 'b');