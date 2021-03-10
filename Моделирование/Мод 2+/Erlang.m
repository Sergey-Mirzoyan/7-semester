clear, clc
 
% ��������� �������������:
k = input("k = ");
lambda = input("lambda = ");
step = input("step = ");
% �������� �� �:
a = input("a = "); % ������ ������
b = input("b = "); % ������� ������
x = linspace(a,b,step); % ��������� �������� �� step �����
% ������� ��������� ������������� ��
w = @(x) lambda.^k * x.^(k-1) .* exp((-1)*lambda*x)/(factorial(k-1));
W = w(x); % ������� ���������
mW = max(W); % ������� ����. ��������

%������� ������������� ��
for i=x
    if i >= 0
        WW = 1 - exp(-lambda*x)
    else
        WW = 0
    end
end


% ������:
grid on 
subplot(4, 1, 1)
plot(x, pdf('Uniform', x, a, b));
subplot(4, 1, 2);
plot(x, cdf('Uniform', x, a, b));

subplot(4, 1, 3);

plot(x,W,'r');
subplot(4, 1, 4);
plot(x, WW, 'b');