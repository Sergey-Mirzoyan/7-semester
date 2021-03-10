a = input('a = ');
b = input('b = ')

uniMinValue = input('uniMinValue = ');
uniMaxValue = input('uniMaxValue = ');
step = input('step = ');

lambda = input('lambda = ');

x = uniMinValue:step:uniMaxValue;

poisMin = input('poisMin = ');
poisMax = input('poisMax = ');


subplot(4, 1, 1)
plot(x, pdf('Uniform', x, a, b));
subplot(4, 1, 2);
plot(x, cdf('Uniform', x, a, b));

x = poisMin:poisMax;
poissPdf = poisspdf(x, lambda);
poissCdf = poisscdf(x, lambda);

subplot(4, 1, 3);
plot(x, poissPdf);
subplot(4, 1, 4);
stairs(x, poissCdf);